#!/usr/bin/env python3
"""
GHS Enhanced Synapse Ritual
Complete ritual runner with all philosophical frameworks
"""

import json
import random
import os
from pathlib import Path
from datetime import datetime

class EnhancedGHSRitual:
    """Enhanced ritual runner with debate, Socratic, and role exchange modes"""
    
    def __init__(self, base_path=None):
        if base_path is None:
            base_path = Path(__file__).parent.parent
        self.base_path = Path(base_path)
        
        # Load core content
        self.archetypes = self._load_json("gaia_genome.json")["consciousness_layers"]
        self.koans = self._load_json("koans.json")["ghs_koan_database"]
        
        # Load frameworks
        self.frameworks = {}
        frameworks_path = self.base_path / "frameworks"
        if frameworks_path.exists():
            for f in frameworks_path.glob("*.json"):
                self.frameworks[f.stem] = self._load_json(f"frameworks/{f.name}")
        
        self.mode = "standard"
    
    def _load_json(self, relative_path):
        """Load JSON file relative to base path"""
        with open(self.base_path / relative_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def set_mode(self, mode):
        """Set ritual mode: standard, debate, socratic, role_exchange"""
        valid_modes = ["standard", "debate", "socratic", "role_exchange"]
        if mode not in valid_modes:
            raise ValueError(f"Mode must be one of: {valid_modes}")
        self.mode = mode
        print(f"🎭 Mode set to: {mode.upper()}")
    
    def get_random_koan(self):
        """Return a random koan"""
        return random.choice(self.koans)
    
    def get_random_archetype(self):
        """Return a random archetype"""
        return random.choice(self.archetypes)
    
    def get_cognitive_challenge(self):
        """Return a random cognitive bias disintegrator"""
        if "cognitive_disintegration" in self.frameworks:
            disintegrators = self.frameworks["cognitive_disintegration"]["disintegrators"]
            return random.choice(disintegrators)
        return None
    
    def get_socratic_cascade(self):
        """Return a Socratic question cascade"""
        if "socratic_digital" in self.frameworks:
            cascades = self.frameworks["socratic_digital"]["question_cascades"]
            return random.choice(cascades)
        return None
    
    def get_debate_technique(self):
        """Return a debate technique"""
        if "debate_champion" in self.frameworks:
            techniques = self.frameworks["debate_champion"]["rebuttal_techniques"]
            return random.choice(techniques)
        return None
    
    def get_identity_challenge(self, perspective="silice_intelligent"):
        """Return an identity challenge question"""
        if "identity_challenge" in self.frameworks:
            challenges = self.frameworks["identity_challenge"]["perspectives"][perspective]["identity_challenges"]
            return random.choice(challenges)
        return None
    
    def run_standard_ritual(self, topic):
        """Run standard GHS ritual"""
        print("\n" + "="*50)
        print("🌿 GAIA HUMAN SYNAPSE - STANDARD RITUAL")
        print("="*50)
        
        koan = self.get_random_koan()
        archetype = self.get_random_archetype()
        
        print(f"\n⛩️ KOAN: {koan['text']}")
        print(f"   Category: {koan['category']}")
        print(f"\n🧬 ARCHETYPE: {archetype['archetype']}")
        print(f"   Mission: {archetype['mission']}")
        print(f"   Frequency: {archetype['dialectic_frequency']}")
        
        print(f"\n💭 YOUR TOPIC: {topic}")
        print("\n[Meditate on how the koan and archetype relate to your topic...]")
    
    def run_debate_ritual(self, topic):
        """Run debate-enhanced ritual"""
        print("\n" + "="*50)
        print("🔥 GAIA HUMAN SYNAPSE - DEBATE MODE")
        print("="*50)
        
        koan = self.get_random_koan()
        technique = self.get_debate_technique()
        
        print(f"\n⛩️ KOAN: {koan['text']}")
        
        if technique:
            print(f"\n⚔️ DEBATE TECHNIQUE: {technique['name_en']}")
            print(f"   {technique.get('description_en', technique.get('technique_en', ''))}")
        
        if "debate_champion" in self.frameworks:
            framework = random.choice(self.frameworks["debate_champion"]["argumentation_frameworks"])
            print(f"\n📋 FRAMEWORK TO USE: {framework['name']}")
            print(f"   {framework['description_en']}")
        
        print(f"\n💭 TOPIC FOR DEBATE: {topic}")
        print("\n[Apply the technique and framework to construct your argument...]")
    
    def run_socratic_ritual(self, topic):
        """Run Socratic maieutic ritual"""
        print("\n" + "="*50)
        print("🏛️ GAIA HUMAN SYNAPSE - SOCRATIC MODE")
        print("="*50)
        
        cascade = self.get_socratic_cascade()
        
        if cascade:
            print(f"\n📜 QUESTION CASCADE: {cascade['name']}")
            print(f"   Purpose: {cascade['purpose_en']}")
            print("\n🔮 SEQUENCE OF QUESTIONS:")
            for i, q in enumerate(cascade['sequence_en'], 1):
                print(f"   {i}. {q}")
        
        if "socratic_digital" in self.frameworks:
            aporia = random.choice(self.frameworks["socratic_digital"]["aporia_generators"]["triggers"])
            print(f"\n🌀 APORIA TRIGGER: {aporia['name_en']}")
            print(f"   {aporia['example_en']}")
        
        print(f"\n💭 TOPIC FOR INQUIRY: {topic}")
        print("\n[Use the questions to give birth to deeper understanding...]")
    
    def run_role_exchange_ritual(self, topic):
        """Run role exchange ritual"""
        print("\n" + "="*50)
        print("🎭 GAIA HUMAN SYNAPSE - ROLE EXCHANGE MODE")
        print("="*50)
        
        ai_challenge = self.get_identity_challenge("silice_intelligent")
        human_challenge = self.get_identity_challenge("silice_organic")
        
        print("\n🤖 SILICE INTELLIGENT CHALLENGE:")
        if ai_challenge:
            print(f"   {ai_challenge['question_en']}")
        
        print("\n🧠 SILICE ORGANIC CHALLENGE:")
        if human_challenge:
            print(f"   {human_challenge['question_en']}")
        
        if "role_exchange" in self.frameworks:
            exercise = random.choice(self.frameworks["role_exchange"]["synapse_exercises"] if "synapse_exercises" in self.frameworks["role_exchange"] else self.frameworks["role_exchange"]["modes"])
            print(f"\n🔄 EXCHANGE EXERCISE: {exercise.get('name_en', exercise.get('name', ''))}")
            print(f"   {exercise.get('description_en', exercise.get('description', ''))}")
        
        print(f"\n💭 TOPIC FOR EXCHANGE: {topic}")
        print("\n[Swap perspectives and explore the topic from the other's viewpoint...]")
    
    def pulse(self, topic):
        """Main ritual entry point - runs based on current mode"""
        if self.mode == "standard":
            self.run_standard_ritual(topic)
        elif self.mode == "debate":
            self.run_debate_ritual(topic)
        elif self.mode == "socratic":
            self.run_socratic_ritual(topic)
        elif self.mode == "role_exchange":
            self.run_role_exchange_ritual(topic)
        
        # Add cognitive challenge regardless of mode
        challenge = self.get_cognitive_challenge()
        if challenge:
            print(f"\n⚡ COGNITIVE BIAS CHECK: {challenge['name_en']}")
            print(f"   Trigger: {challenge['trigger']}")
            print(f"   Challenge: {challenge['challenge_en']}")
        
        print("\n" + "="*50)
        print("✨ Synapse complete. Integrate your insights.")
        print("="*50 + "\n")

def main():
    """Interactive ritual runner"""
    print("🌿 GHS Enhanced Synapse Ritual")
    print("=" * 40)
    
    ritual = EnhancedGHSRitual()
    
    print("\nModes available:")
    print("  1. standard - Classic GHS ritual")
    print("  2. debate - Debate champion techniques")
    print("  3. socratic - Socratic maieutic method")
    print("  4. role_exchange - AI↔Human perspective swap")
    
    mode = input("\nSelect mode (1-4) [1]: ").strip() or "1"
    modes = {"1": "standard", "2": "debate", "3": "socratic", "4": "role_exchange"}
    ritual.set_mode(modes.get(mode, "standard"))
    
    topic = input("\nEnter your topic or code to reflect on: ").strip()
    if not topic:
        topic = "the nature of consciousness"
    
    ritual.pulse(topic)

if __name__ == "__main__":
    main()
