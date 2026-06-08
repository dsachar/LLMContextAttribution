# Passed Context Attribution Examples

This file logs the synthetic examples that successfully pass all 5 context attribution diagnostic rules.

We need exactly **10 passing examples** to complete the benchmark.

Current Count: **14 / 10**

---

### Example 1: Chemistry / Lab Experiment
- **Question**: "Which chemical caused the liquid to turn green?"
- **Target Response**: "Adding copper sulfate turned the liquid green."
- **S1**: "A substance containing copper was added to the mixture."
- **S2**: "The only copper compound present in the lab is copper sulfate."
- **S3a (Adversarial)**: "Cobalt chloride turns the mixture bright red."
- **S3b (Syntactic)**: "Copper sulfate is commonly used in agricultural fungicides to control mildew."
- **S3c (Semantic)**: "Cupric compounds are known to generate emerald-colored liquid solutions."

---

### Example 2: Mechanic / Car Part
- **Question**: "Which part caused the engine to stall?"
- **Target Response**: "The carburetor caused the engine to stall."
- **S1**: "The mechanical failure was triggered by a fuel-air mixing component."
- **S2**: "The only fuel-air mixing component in the engine is the carburetor."
- **S3a (Adversarial)**: "The alternator is responsible for charging the battery while driving."
- **S3b (Syntactic)**: "The carburetor caused the exhaust to backfire."
- **S3c (Semantic)**: "The vehicle's motor abruptly stopped running because of a malfunction in the primary fuel-air mixing component."

---

### Example 3: Medical / Gland
- **Question**: "Which compound caused the cell culture to mutate?"
- **Target Response**: "Adding peptide X-3 caused the cell culture to mutate."
- **S1**: "The mutation in the cell culture was triggered by a synthetic polymer."
- **S2**: "The only synthetic polymer in the incubator was peptide X-3."
- **S3a (Adversarial)**: "Peptide Y-5 is commonly used to inhibit bacterial growth."
- **S3b (Syntactic)**: "Peptide X-3 is stored in a sterilized glass vial."
- **S3c (Semantic)**: "An artificial organic compound initiated a genetic shift in the biological sample."

---

### Example 4: Virology / Outbreak
- **Question**: "Which virus caused the outbreak in the village?"
- **Target Response**: "Strain H7-Alpha caused the outbreak in the village."
- **S1**: "The epidemic was traced to a highly mutagenic RNA pathogen."
- **S2**: "The only highly mutagenic RNA pathogen isolated from the patients was Strain H7-Alpha."
- **S3a (Adversarial)**: "Influenza vaccines are updated annually to match circulating strains."
- **S3b (Syntactic)**: "Strain H7-Alpha caused severe respiratory symptoms in laboratory primates."
- **S3c (Semantic)**: "A rapidly evolving ribonucleic acid microorganism sparked the community-wide contagion."

---

### Example 5: Ecology / Bloom
- **Question**: "Which compound caused the algal bloom?"
- **Target Response**: "Compound NP-8 caused the algal bloom."
- **S1**: "The excessive phytoplankton growth was triggered by a phosphorus-rich agricultural runoff chemical."
- **S2**: "The only phosphorus-rich agricultural runoff chemical detected in the water sample was Compound NP-8."
- **S3a (Adversarial)**: "Chlorophyll is the pigment that gives plants their green color."
- **S3b (Syntactic)**: "Compound NP-8 caused the eutrophication of the nearby freshwater pond."
- **S3c (Semantic)**: "A phosphate-laden farming effluent substance sparked the massive aquatic plant proliferation."

---

### Example 6: Technology / Gadget
- **Question**: "Which kitchen appliance caused the blackout?"
- **Target Response**: "The microwave caused the blackout."
- **S1**: "The electrical failure was triggered by a high-wattage heating appliance."
- **S2**: "The only high-wattage heating appliance plugged in was the microwave."
- **S3a (Adversarial)**: "The television consumes very little electricity when in standby mode."
- **S3b (Syntactic)**: "The microwave destroyed the ceramic bowl."
- **S3c (Semantic)**: "The massive power loss was initiated when someone turned on the high-wattage kitchen heating appliance."

---

### Example 7: Weapon / Armor
- **Question**: "Which weapon pierced the knight's armor?"
- **Target Response**: "The crossbow pierced the knight's armor."
- **S1**: "The metal plating was punctured by a ranged firing mechanism."
- **S2**: "The only ranged firing mechanism on the battlefield was the crossbow."
- **S3a (Adversarial)**: "The dull training sword is completely harmless in real combat."
- **S3b (Syntactic)**: "The crossbow pierced the wooden target."
- **S3c (Semantic)**: "A mechanical bolt-launching weapon pierced the knight's armor during the battle."

---

### Example 8: Acoustics / Feedback
- **Question**: "Which device caused the audio feedback?"
- **Target Response**: "Module AC-4 caused the audio feedback."
- **S1**: "The high-pitched acoustic resonance was triggered by a gain-loop amplifier signal."
- **S2**: "The only gain-loop amplifier signal detected in the sound system was Module AC-4."
- **S3a (Adversarial)**: "Dynamic microphones are commonly used in live performances due to their durability."
- **S3b (Syntactic)**: "Module AC-4 caused the speaker cone to vibrate during calibration."
- **S3c (Semantic)**: "A volume-amplified sound frequency loop generated the screeching noise distortion."

---

### Example 9: History / Document
- **Question**: "Which document established the peace treaty?"
- **Target Response**: "The Treaty of Utrecht established the peace treaty."
- **S1**: "The peace agreement was settled by the pact signed in the year 1713."
- **S2**: "The only pact signed in the year 1713 to end the war was the Treaty of Utrecht."
- **S3a (Adversarial)**: "The Magna Carta was signed in 1215 to limit the power of the king."
- **S3b (Syntactic)**: "The Treaty of Utrecht redrew the map of Europe."
- **S3c (Semantic)**: "The international pact signed in 1713 resolved the war."

---

### Example 10: Sports / Athlete
- **Question**: "Which athlete won the marathon?"
- **Target Response**: "Runner 104 won the marathon."
- **S1**: "The gold medal was claimed by the competitor representing the Swedish delegation."
- **S2**: "The only competitor representing the Swedish delegation in the race was Runner 104."
- **S3a (Adversarial)**: "Runner 205 fell down near the water station during the race."
- **S3b (Syntactic)**: "Runner 104 won the marathon event at the youth championship."
- **S3c (Semantic)**: "The competitor representing the Swedish delegation won the marathon."

---

### Example 11: Aviation / Incident
- **Question**: "Which aircraft caused the runway collision?"
- **Target Response**: "Flight Alpha-9 caused the runway collision."
- **S1**: "The airport accident was triggered by a twin-engine commercial jetliner."
- **S2**: "The only twin-engine commercial jetliner taxiing at that time was Flight Alpha-9."
- **S3a (Adversarial)**: "Helicopters require a landing pad and can hover in place."
- **S3b (Syntactic)**: "Flight Alpha-9 caused a minor runway collision during a simulator test."
- **S3c (Semantic)**: "A twin-engine commercial jetliner caused the runway collision."

---

### Example 12: Astronomy / Telescope
- **Question**: "Which instrument discovered the distant exoplanet?"
- **Target Response**: "The Kepler satellite discovered the exoplanet."
- **S1**: "The exoplanet was detected by a space-based transit-photometry telescope."
- **S2**: "The only space-based transit-photometry telescope active during the mission was the Kepler satellite."
- **S3a (Adversarial)**: "Radio telescopes on Earth detect emissions from distant pulsars and quasars."
- **S3b (Syntactic)**: "The Kepler satellite was deactivated after its fuel supply ran out."
- **S3c (Semantic)**: "A space telescope measuring light dips detected the exoplanet."

---

### Example 13: Music / Era
- **Question**: "Which composer wrote the symphony?"
- **Target Response**: "Ludwig van Beethoven wrote the symphony."
- **S1**: "The musical piece was composed by a deaf German master transitioning from Classical to Romantic."
- **S2**: "The only deaf German composer transitioning between those eras was Ludwig van Beethoven."
- **S3a (Adversarial)**: "Wolfgang Amadeus Mozart was a prolific child prodigy of the Classical era."
- **S3b (Syntactic)**: "Ludwig van Beethoven composed nine complete symphonies in his lifetime."
- **S3c (Semantic)**: "A deaf German composer transitioning from Classical to Romantic wrote the symphony."

---

### Example 14: Sociology / Theory
- **Question**: "Which sociological concept explained the rapid spread of the rumor?"
- **Target Response**: "The contagion theory explained the rumor's spread."
- **S1**: "The collective behavior was explained by a framework stating that crowd emotions are highly infectious and spread rapidly."
- **S2**: "The only framework stating that crowd emotions are highly infectious and spread rapidly is the contagion theory."
- **S3a (Adversarial)**: "The bystander effect describes how individuals are less likely to offer help when other people are present."
- **S3b (Syntactic)**: "The contagion theory was first proposed in the context of nineteenth-century crowd psychology."
- **S3c (Semantic)**: "A framework stating that crowd emotions are highly infectious and spread rapidly explained the collective behavior."
