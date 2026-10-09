//! Print `module!import` for every import of each PE32 file given on the command line.
use pelite::pe32::{Pe, PeFile};
use std::collections::BTreeSet;

fn main() {
    let mut all = BTreeSet::new();
    for path in std::env::args().skip(1) {
        let Ok(bytes) = std::fs::read(&path) else { continue };
        let Ok(pe) = PeFile::from_bytes(&bytes) else { continue };
        let Ok(imports) = pe.imports() else { continue };
        for desc in imports {
            let Ok(dll) = desc.dll_name() else { continue };
            let Ok(names) = desc.int() else { continue };
            for import in names.flatten() {
                if let pelite::pe32::imports::Import::ByName { name, .. } = import {
                    all.insert(format!(
                        "{}!{}",
                        dll.to_string().to_ascii_lowercase(),
                        name
                    ));
                }
            }
        }
    }
    for line in all {
        println!("{line}");
    }
}
