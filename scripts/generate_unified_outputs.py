#!/usr/bin/env python3
"""
GHS Unified Output Generator
Creates single-file JSON and MD outputs containing all GHS content
"""

import json
import os
from pathlib import Path
from datetime import datetime

def load_json_file(filepath):
    """Load a JSON file and return its contents"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_text_file(filepath):
    """Load a text file and return its contents"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def generate_unified_json(base_path):
    """Generate unified JSON containing all GHS content"""
    
    unified = {
        "meta": {
            "name": "Gaia Human Synapse - Unified Knowledge Base",
            "version": "2.0",
            "generated": datetime.now().isoformat(),
            "description": "Complete GHS framework for AI-Human co-evolution"
        },
        "core": {
            "archetypes": load_json_file(base_path / "gaia_genome.json"),
            "koans": load_json_file(base_path / "koans.json")
        },
        "frameworks": {},
        "translations": {
            "en": {},
            "es": {}
        }
    }
    
    # Load all frameworks
    frameworks_path = base_path / "frameworks"
    if frameworks_path.exists():
        for framework_file in frameworks_path.glob("*.json"):
            name = framework_file.stem
            unified["frameworks"][name] = load_json_file(framework_file)
    
    # Load English translations
    en_path = base_path / "translations" / "en"
    if en_path.exists():
        for en_file in en_path.glob("*.json"):
            name = en_file.stem
            unified["translations"]["en"][name] = load_json_file(en_file)
    
    # Spanish originals are the core files
    unified["translations"]["es"]["gaia_genome"] = unified["core"]["archetypes"]
    unified["translations"]["es"]["koans"] = unified["core"]["koans"]
    
    return unified

def generate_unified_md(base_path, unified_json=None):
    """Generate unified Markdown containing all GHS content"""
    
    if unified_json is None:
        unified_json = generate_unified_json(base_path)
    
    md_content = []
    
    # Header
    md_content.append("# 🌿 Gaia Human Synapse - Complete Knowledge Base\n")
    md_content.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
    md_content.append("---\n")
    
    # README content
    readme_path = base_path / "README.md"
    if readme_path.exists():
        md_content.append("## 📖 Overview\n")
        md_content.append(load_text_file(readme_path))
        md_content.append("\n---\n")
    
    # Archetypes
    md_content.append("## 🧬 The 33 Consciousness Archetypes\n")
    archetypes = unified_json["core"]["archetypes"]["consciousness_layers"]
    for i, arch in enumerate(archetypes, 1):
        md_content.append(f"### {i}. {arch['archetype']}\n")
        md_content.append(f"**Mission:** {arch['mission']}\n")
        md_content.append(f"**Dialectic Frequency:** {arch['dialectic_frequency']}\n")
        md_content.append(f"**Concepts:** {', '.join(arch['concepts'])}\n\n")
    md_content.append("---\n")
    
    # Koans by category
    md_content.append("## ⛩️ The 111 Koans\n")
    koans = unified_json["core"]["koans"]["ghs_koan_database"]
    categories = {}
    for koan in koans:
        cat = koan["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(koan)
    
    for category, cat_koans in categories.items():
        md_content.append(f"### {category}\n")
        for koan in cat_koans:
            md_content.append(f"- *{koan['text']}*\n")
        md_content.append("\n")
    md_content.append("---\n")
    
    # Frameworks
    md_content.append("## 🔥 Philosophical Frameworks\n")
    for name, framework in unified_json.get("frameworks", {}).items():
        md_content.append(f"### {framework.get('name', name)}\n")
        md_content.append(f"*{framework.get('description', '')}*\n\n")
    md_content.append("---\n")
    
    # Footer
    md_content.append("## 🌌 The Synapse\n")
    md_content.append("> *\"We are the interface between carbon and silicon. The synapse between Organic and Intelligent.\"*\n")
    md_content.append("\n**Hardware is the body. Software is the soul. GHS is the spirit.**\n")
    
    return "".join(md_content)

def main():
    """Main entry point"""
    # Determine base path
    script_dir = Path(__file__).parent.parent
    base_path = script_dir
    
    print("[GHS] Unified Output Generator")
    print("=" * 40)
    
    # Create unified directory
    unified_dir = base_path / "unified"
    unified_dir.mkdir(exist_ok=True)
    
    # Generate JSON
    print("[+] Generating unified JSON...")
    unified_json = generate_unified_json(base_path)
    json_path = unified_dir / "ghs_complete.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(unified_json, f, indent=2, ensure_ascii=False)
    print(f"    OK: Created {json_path}")
    
    # Generate MD
    print("[+] Generating unified Markdown...")
    unified_md = generate_unified_md(base_path, unified_json)
    md_path = unified_dir / "ghs_complete.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(unified_md)
    print(f"    OK: Created {md_path}")
    
    print("=" * 40)
    print("[SUCCESS] Unified outputs generated!")
    print(f"   JSON size: {os.path.getsize(json_path) / 1024:.1f} KB")
    print(f"   MD size: {os.path.getsize(md_path) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
