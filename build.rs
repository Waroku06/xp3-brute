fn main() {
    println!("cargo:rerun-if-changed=magic/krkr");
    #[cfg(feature = "python")]
    pyo3_build_config::add_extension_module_link_args();

    // unicorn-engine (QEMU) emits 16-byte atomics (__atomic_store_16, ...) that are
    // provided by libatomic on Linux; rust-lld does not link it implicitly.
    if std::env::var("CARGO_CFG_TARGET_OS").as_deref() == Ok("linux")
        && std::env::var("CARGO_CFG_TARGET_ENV").as_deref() == Ok("gnu")
        && libatomic_available()
    {
        println!("cargo:rustc-link-lib=atomic");
    }
}

fn libatomic_available() -> bool {
    let cc = std::env::var("CC").unwrap_or_else(|_| "cc".to_string());
    ["libatomic.so", "libatomic.a"].iter().any(|name| {
        std::process::Command::new(&cc)
            .arg(format!("-print-file-name={name}"))
            .output()
            .ok()
            .map(|o| String::from_utf8_lossy(&o.stdout).trim().contains('/'))
            .unwrap_or(false)
    })
}
