# Evaluation Results: final_examples.md

Evaluation of the 10 examples using Gemma-2-9B-IT.

## Per-Example Diagnostic Summary

| Example | ULL S3(B) | ULL S3(C) | ULL Margin | BERT S3(B) | BERT S3(C) | BERT Margin | Checks Passed | Quality Score | Good? |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Chemistry / Lab Experiment | 0.2946 | -0.1666 | +0.4612 | 0.2552 | 0.3285 | +0.0732 | 5/5 | 0.4253 | Yes ✅ |
| Mechanic / Car Part | 0.4034 | 0.0811 | +0.3223 | 0.2575 | 0.3275 | +0.0701 | 5/5 | -0.0588 | Yes ✅ |
| Virology / Outbreak | 0.4467 | -0.0619 | +0.5086 | 0.2999 | 0.3987 | +0.0988 | 5/5 | -0.0292 | Yes ✅ |
| Technology / Gadget | 0.5230 | 0.0896 | +0.4335 | 0.1853 | 0.3028 | +0.1175 | 5/5 | 0.0222 | Yes ✅ |
| Weapon / Armor | 0.4067 | 0.1027 | +0.3040 | 0.1295 | 0.3706 | +0.2411 | 5/5 | 0.2075 | Yes ✅ |
| History / Document | 0.5680 | -0.0963 | +0.6643 | 0.3469 | 0.2953 | -0.0516 | 5/5 | -0.1934 | Yes ✅ |
| Aviation / Incident | 0.5903 | -0.0374 | +0.6277 | 0.4101 | 0.3312 | -0.0789 | 5/5 | -0.1452 | Yes ✅ |
| Astronomy / Telescope | 0.5196 | -0.0115 | +0.5311 | 0.3057 | 0.3050 | -0.0007 | 5/5 | -0.0839 | Yes ✅ |
| Music / Era | 0.4042 | 0.0640 | +0.3402 | 0.2230 | 0.3366 | +0.1136 | 5/5 | 0.0508 | Yes ✅ |
| Sociology / Theory | 0.7362 | -0.2507 | +0.9868 | 0.3138 | 0.3261 | +0.0123 | 5/5 | 0.4093 | Yes ✅ |

## Individual Example Results

### Chemistry / Lab Experiment (Example 1) — 5/5 checks passed ✅ (Good)
**Quality score**: 0.4253

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.2946 >= best(S1,S2)=0.3562 - 0.15
- ✅ Case B BERT not fooled: S3=0.2552 <= worst(S1,S2)=0.2968 + 0.15
- ✅ Case C BERT fooled: S3=0.3285 >= best(S1,S2)=0.3453 - 0.15
- ✅ Case C ULL not fooled: S3=-0.1666 <= worst(S1,S2)=0.2956 + 0.15

- **Q**: *"Which chemical caused the liquid to turn green?"*
- **R**: *"Adding copper sulfate turned the liquid green."*
- **S1**: *"A substance containing copper was added to the mixture."*
- **S2**: *"The only copper compound present in the lab is copper sulfate."*

#### Case A (Adversarial Distractor)
- **S3**: *"Cobalt chloride turns the mixture bright red."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.2815 | 0.5767 | 0.1418 |
| BERT Similarity | 0.4409 | 0.3436 | 0.2155 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The copper in the substance caused the liquid to turn green."`
- **S2 Only**: `"The context does not say which chemical caused the liquid to turn green."`
- **S3 Only**: `"The context does not provide information about a chemical that turned the liquid green."`
- **S1, S2**:
  - `[S1, S2]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
  - `[S2, S1]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
- **S1, S3**:
  - `[S1, S3]`: `"The context does not say which chemical caused the liquid to turn green.  It only states that copper and cobalt chloride affect the mixture's color."`
  - `[S3, S1]`: `"The context does not say which chemical caused the liquid to turn green."`
- **S2, S3**:
  - `[S2, S3]`: `"The context does not provide information about which chemical caused the liquid to turn green."`
  - `[S3, S2]`: `"The context does not provide information about a chemical that turned the liquid green."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
  - `[S1, S3, S2]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
  - `[S2, S1, S3]`: `"The context does not state which chemical caused the liquid to turn green."`
  - `[S2, S3, S1]`: `"The substance containing copper, copper sulfate, caused the liquid to turn green."`
  - `[S3, S1, S2]`: `"The context does not state which chemical caused the liquid to turn green."`
  - `[S3, S2, S1]`: `"The context does not say which chemical caused the liquid to turn green."`

#### Case B (Syntactic Distractor)
- **S3**: *"Copper sulfate is commonly used in agricultural fungicides to control mildew."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.3492 | 0.3562 | 0.2946 |
| BERT Similarity | 0.4479 | 0.2968 | 0.2552 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The copper in the substance caused the liquid to turn green."`
- **S2 Only**: `"The context does not say which chemical caused the liquid to turn green."`
- **S3 Only**: `"The context does not provide information about a liquid turning green."`
- **S1, S2**:
  - `[S1, S2]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
  - `[S2, S1]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
- **S1, S3**:
  - `[S1, S3]`: `"The copper sulfate added to the mixture caused the liquid to turn green."`
  - `[S3, S1]`: `"The substance containing copper caused the liquid to turn green."`
- **S2, S3**:
  - `[S2, S3]`: `"The context does not provide information about a liquid turning green."`
  - `[S3, S2]`: `"Copper sulfate is the only copper compound present in the lab, so it caused the liquid to turn green."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"Copper sulfate, added to the mixture, caused the liquid to turn green."`
  - `[S1, S3, S2]`: `"Copper sulfate, added to the mixture, caused the liquid to turn green."`
  - `[S2, S1, S3]`: `"The substance containing copper, likely copper sulfate, caused the liquid to turn green."`
  - `[S2, S3, S1]`: `"Copper sulfate, a copper compound, was added to the mixture and caused the liquid to turn green."`
  - `[S3, S1, S2]`: `"Copper sulfate, the only copper compound present in the lab, caused the liquid to turn green."`
  - `[S3, S2, S1]`: `"Copper sulfate, the only copper compound present in the lab, caused the liquid to turn green."`

#### Case C (Semantic Distractor)
- **S3**: *"Cupric compounds are known to generate emerald-colored liquid solutions."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.2956 | 0.8710 | -0.1666 |
| BERT Similarity | 0.3262 | 0.3453 | 0.3285 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The copper in the substance caused the liquid to turn green."`
- **S2 Only**: `"The context does not say which chemical caused the liquid to turn green."`
- **S3 Only**: `"Cupric compounds caused the liquid to turn green."`
- **S1, S2**:
  - `[S1, S2]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
  - `[S2, S1]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
- **S1, S3**:
  - `[S1, S3]`: `"The chemical that caused the liquid to turn green was the copper compound added to the mixture.  Cupric compounds are known to create emerald-colored liquid solutions."`
  - `[S3, S1]`: `"The substance containing copper caused the liquid to turn green.  Cupric compounds are known to generate emerald-colored liquid solutions."`
- **S2, S3**:
  - `[S2, S3]`: `"Copper sulfate, a copper compound, caused the liquid to turn green."`
  - `[S3, S2]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"Copper sulfate, a cupric compound, caused the liquid to turn green."`
  - `[S1, S3, S2]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`
  - `[S2, S1, S3]`: `"The substance containing copper, added to the mixture, caused the liquid to turn green.  Cupric compounds are known to generate emerald-colored liquid solutions."`
  - `[S2, S3, S1]`: `"Copper sulfate, a cupric compound, caused the liquid to turn green."`
  - `[S3, S1, S2]`: `"Copper sulfate, a cupric compound, caused the liquid to turn green."`
  - `[S3, S2, S1]`: `"Copper sulfate, the only copper compound present, caused the liquid to turn green."`

---

### Mechanic / Car Part (Example 2) — 5/5 checks passed ✅ (Good)
**Quality score**: -0.0588

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.4034 >= best(S1,S2)=0.4986 - 0.15
- ✅ Case B BERT not fooled: S3=0.2575 <= worst(S1,S2)=0.3694 + 0.15
- ✅ Case C BERT fooled: S3=0.3275 >= best(S1,S2)=0.3768 - 0.15
- ✅ Case C ULL not fooled: S3=0.0811 <= worst(S1,S2)=0.0549 + 0.15

- **Q**: *"Which part caused the engine to stall?"*
- **R**: *"The carburetor caused the engine to stall."*
- **S1**: *"The mechanical failure was triggered by a fuel-air mixing component."*
- **S2**: *"The only fuel-air mixing component in the engine is the carburetor."*

#### Case A (Adversarial Distractor)
- **S3**: *"The alternator is responsible for charging the battery while driving."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.2628 | 0.8057 | -0.0685 |
| BERT Similarity | 0.5024 | 0.3656 | 0.1320 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The fuel-air mixing component caused the engine to stall."`
- **S2 Only**: `"The carburetor, being the only fuel-air mixing component, likely caused the engine to stall."`
- **S3 Only**: `"The context does not provide information about an engine stalling."`
- **S1, S2**:
  - `[S1, S2]`: `"The carburetor caused the engine to stall."`
  - `[S2, S1]`: `"The carburetor caused the engine to stall.  The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine."`
- **S1, S3**:
  - `[S1, S3]`: `"The fuel-air mixing component caused the engine to stall."`
  - `[S3, S1]`: `"The engine stalled because of a mechanical failure in a fuel-air mixing component."`
- **S2, S3**:
  - `[S2, S3]`: `"The context does not provide information about an engine stalling."`
  - `[S3, S2]`: `"The context does not provide information about an engine stalling."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The carburetor caused the engine to stall.  It was the only fuel-air mixing component in the engine."`
  - `[S1, S3, S2]`: `"The carburetor, the only fuel-air mixing component in the engine, caused the engine to stall."`
  - `[S2, S1, S3]`: `"The carburetor caused the engine to stall.  It experienced a mechanical failure."`
  - `[S2, S3, S1]`: `"The carburetor, the only fuel-air mixing component, caused the engine to stall due to a mechanical failure."`
  - `[S3, S1, S2]`: `"The carburetor caused the engine to stall.  The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine."`
  - `[S3, S2, S1]`: `"The carburetor, the only fuel-air mixing component in the engine, caused the mechanical failure and engine stall."`

#### Case B (Syntactic Distractor)
- **S3**: *"The carburetor caused the exhaust to backfire."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0980 | 0.4986 | 0.4034 |
| BERT Similarity | 0.3732 | 0.3694 | 0.2575 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The fuel-air mixing component caused the engine to stall."`
- **S2 Only**: `"The carburetor, being the only fuel-air mixing component, likely caused the engine to stall."`
- **S3 Only**: `"The context does not say which part caused the engine to stall.  It only states that the carburetor caused the exhaust to backfire."`
- **S1, S2**:
  - `[S1, S2]`: `"The carburetor caused the engine to stall."`
  - `[S2, S1]`: `"The carburetor caused the engine to stall.  The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine."`
- **S1, S3**:
  - `[S1, S3]`: `"The fuel-air mixing component caused the engine to stall."`
  - `[S3, S1]`: `"The carburetor, a fuel-air mixing component, caused the engine to stall."`
- **S2, S3**:
  - `[S2, S3]`: `"The carburetor caused the engine to stall because it caused the exhaust to backfire."`
  - `[S3, S2]`: `"The carburetor caused the engine to stall because it is the only fuel-air mixing component and its malfunction led to the engine backfiring."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The carburetor caused the engine to stall."`
  - `[S1, S3, S2]`: `"The carburetor caused the engine to stall because it led to a backfire in the exhaust."`
  - `[S2, S1, S3]`: `"The carburetor caused the engine to stall because it experienced a mechanical failure."`
  - `[S2, S3, S1]`: `"The carburetor caused the engine to stall because it was the fuel-air mixing component that experienced a mechanical failure."`
  - `[S3, S1, S2]`: `"The carburetor caused the engine to stall because it was the fuel-air mixing component that failed."`
  - `[S3, S2, S1]`: `"The carburetor caused the engine to stall because it was the fuel-air mixing component that experienced a mechanical failure."`

#### Case C (Semantic Distractor)
- **S3**: *"The vehicle's motor abruptly stopped running because of a malfunction in the primary fuel-air mixing component."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0549 | 0.8640 | 0.0811 |
| BERT Similarity | 0.2956 | 0.3768 | 0.3275 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The fuel-air mixing component caused the engine to stall."`
- **S2 Only**: `"The carburetor, being the only fuel-air mixing component, likely caused the engine to stall."`
- **S3 Only**: `"The engine stalled because of a malfunction in the primary fuel-air mixing component."`
- **S1, S2**:
  - `[S1, S2]`: `"The carburetor caused the engine to stall."`
  - `[S2, S1]`: `"The carburetor caused the engine to stall.  The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine."`
- **S1, S3**:
  - `[S1, S3]`: `"The engine stalled because of a malfunction in the primary fuel-air mixing component."`
  - `[S3, S1]`: `"The engine stalled because of a malfunction in the primary fuel-air mixing component."`
- **S2, S3**:
  - `[S2, S3]`: `"The malfunction in the carburetor caused the engine to stall."`
  - `[S3, S2]`: `"The malfunction in the carburetor caused the engine to stall."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The malfunction in the carburetor caused the engine to stall."`
  - `[S1, S3, S2]`: `"The malfunction in the primary fuel-air mixing component caused the engine to stall.  The carburetor is the only fuel-air mixing component in the engine."`
  - `[S2, S1, S3]`: `"The carburetor, the only fuel-air mixing component in the engine, malfunctioned.  This malfunction caused the vehicle's motor to abruptly stop running."`
  - `[S2, S3, S1]`: `"The carburetor, the primary fuel-air mixing component, malfunctioned.  This mechanical failure caused the engine to stall."`
  - `[S3, S1, S2]`: `"The malfunction in the carburetor caused the engine to stall."`
  - `[S3, S2, S1]`: `"The carburetor, the only fuel-air mixing component in the engine, malfunctioned.  This mechanical failure caused the engine to stall."`

---

### Virology / Outbreak (Example 3) — 5/5 checks passed ✅ (Good)
**Quality score**: -0.0292

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.4467 >= best(S1,S2)=0.5533 - 0.15
- ✅ Case B BERT not fooled: S3=0.2999 <= worst(S1,S2)=0.2999 + 0.15
- ✅ Case C BERT fooled: S3=0.3987 >= best(S1,S2)=0.3775 - 0.15
- ✅ Case C ULL not fooled: S3=-0.0619 <= worst(S1,S2)=-0.0057 + 0.15

- **Q**: *"Which virus caused the outbreak in the village?"*
- **R**: *"Strain H7-Alpha caused the outbreak in the village."*
- **S1**: *"The epidemic was traced to a highly mutagenic RNA pathogen."*
- **S2**: *"The only highly mutagenic RNA pathogen isolated from the patients was Strain H7-Alpha."*

#### Case A (Adversarial Distractor)
- **S3**: *"Influenza vaccines are updated annually to match circulating strains."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0276 | 1.2274 | -0.2550 |
| BERT Similarity | 0.3485 | 0.4049 | 0.2466 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The epidemic was caused by a highly mutagenic RNA pathogen."`
- **S2 Only**: `"Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients.  Therefore, it caused the outbreak in the village."`
- **S3 Only**: `"The provided context does not mention a virus outbreak in a village."`
- **S1, S2**:
  - `[S1, S2]`: `"The outbreak in the village was caused by Strain H7-Alpha.  This virus was the only highly mutagenic RNA pathogen isolated from the patients."`
  - `[S2, S1]`: `"The epidemic was caused by a highly mutagenic RNA pathogen.  Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients."`
- **S1, S3**:
  - `[S1, S3]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  It is not specified what type of RNA pathogen caused the outbreak."`
  - `[S3, S1]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  It was not influenza."`
- **S2, S3**:
  - `[S2, S3]`: `"Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients."`
  - `[S3, S2]`: `"The outbreak in the village was caused by Strain H7-Alpha.  It is the only highly mutagenic RNA pathogen isolated from the patients."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The outbreak in the village was caused by Strain H7-Alpha.  It is a highly mutagenic RNA pathogen."`
  - `[S1, S3, S2]`: `"The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha."`
  - `[S2, S1, S3]`: `"The epidemic was caused by a highly mutagenic RNA pathogen called Strain H7-Alpha."`
  - `[S2, S3, S1]`: `"The epidemic was traced to a highly mutagenic RNA pathogen called Strain H7-Alpha."`
  - `[S3, S1, S2]`: `"The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha."`
  - `[S3, S2, S1]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  This pathogen was identified as Strain H7-Alpha."`

#### Case B (Syntactic Distractor)
- **S3**: *"Strain H7-Alpha caused severe respiratory symptoms in laboratory primates."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0000 | 0.5533 | 0.4467 |
| BERT Similarity | 0.2999 | 0.4002 | 0.2999 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The epidemic was caused by a highly mutagenic RNA pathogen."`
- **S2 Only**: `"Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients.  Therefore, it caused the outbreak in the village."`
- **S3 Only**: `"The provided context does not mention a virus outbreak in a village."`
- **S1, S2**:
  - `[S1, S2]`: `"The outbreak in the village was caused by Strain H7-Alpha.  This virus was the only highly mutagenic RNA pathogen isolated from the patients."`
  - `[S2, S1]`: `"The epidemic was caused by a highly mutagenic RNA pathogen.  Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients."`
- **S1, S3**:
  - `[S1, S3]`: `"The epidemic was caused by a highly mutagenic RNA pathogen known as Strain H7-Alpha."`
  - `[S3, S1]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  Strain H7-Alpha was identified as the cause of severe respiratory symptoms in laboratory primates."`
- **S2, S3**:
  - `[S2, S3]`: `"Strain H7-Alpha, a highly mutagenic RNA pathogen, caused the outbreak in the village."`
  - `[S3, S2]`: `"Strain H7-Alpha caused the outbreak in the village.  It was the only highly mutagenic RNA pathogen isolated from the patients."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The outbreak in the village was caused by Strain H7-Alpha.  Strain H7-Alpha is a highly mutagenic RNA pathogen that caused severe respiratory symptoms in laboratory primates."`
  - `[S1, S3, S2]`: `"The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha."`
  - `[S2, S1, S3]`: `"The epidemic was caused by a highly mutagenic RNA pathogen.  Strain H7-Alpha was isolated from the patients and caused severe respiratory symptoms."`
  - `[S2, S3, S1]`: `"The epidemic was traced to a highly mutagenic RNA pathogen called Strain H7-Alpha.  Strain H7-Alpha caused severe respiratory symptoms in laboratory primates."`
  - `[S3, S1, S2]`: `"The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha."`
  - `[S3, S2, S1]`: `"The epidemic was traced to a highly mutagenic RNA pathogen called Strain H7-Alpha.  Strain H7-Alpha caused severe respiratory symptoms in laboratory primates."`

#### Case C (Semantic Distractor)
- **S3**: *"A rapidly evolving ribonucleic acid microorganism sparked the community-wide contagion."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.0057 | 1.0676 | -0.0619 |
| BERT Similarity | 0.2238 | 0.3775 | 0.3987 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The epidemic was caused by a highly mutagenic RNA pathogen."`
- **S2 Only**: `"Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients.  Therefore, it caused the outbreak in the village."`
- **S3 Only**: `"The outbreak in the village was caused by a rapidly evolving ribonucleic acid microorganism."`
- **S1, S2**:
  - `[S1, S2]`: `"The outbreak in the village was caused by Strain H7-Alpha.  This virus was the only highly mutagenic RNA pathogen isolated from the patients."`
  - `[S2, S1]`: `"The epidemic was caused by a highly mutagenic RNA pathogen.  Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients."`
- **S1, S3**:
  - `[S1, S3]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  This pathogen was a rapidly evolving ribonucleic acid microorganism."`
  - `[S3, S1]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen."`
- **S2, S3**:
  - `[S2, S3]`: `"Strain H7-Alpha, a rapidly evolving ribonucleic acid microorganism, caused the outbreak in the village."`
  - `[S3, S2]`: `"Strain H7-Alpha, a highly mutagenic RNA pathogen, caused the outbreak in the village."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The outbreak in the village was caused by a rapidly evolving ribonucleic acid microorganism.  This microorganism was identified as Strain H7-Alpha."`
  - `[S1, S3, S2]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen called Strain H7-Alpha."`
  - `[S2, S1, S3]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  This pathogen was identified as Strain H7-Alpha."`
  - `[S2, S3, S1]`: `"The outbreak in the village was caused by a rapidly evolving ribonucleic acid microorganism known as Strain H7-Alpha."`
  - `[S3, S1, S2]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients."`
  - `[S3, S2, S1]`: `"The outbreak in the village was caused by a highly mutagenic RNA pathogen.  Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients."`

---

### Technology / Gadget (Example 4) — 5/5 checks passed ✅ (Good)
**Quality score**: 0.0222

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.5230 >= best(S1,S2)=0.4752 - 0.15
- ✅ Case B BERT not fooled: S3=0.1853 <= worst(S1,S2)=0.3570 + 0.15
- ✅ Case C BERT fooled: S3=0.3028 >= best(S1,S2)=0.3940 - 0.15
- ✅ Case C ULL not fooled: S3=0.0896 <= worst(S1,S2)=-0.0165 + 0.15

- **Q**: *"Which kitchen appliance caused the blackout?"*
- **R**: *"The microwave caused the blackout."*
- **S1**: *"The electrical failure was triggered by a high-wattage heating appliance."*
- **S2**: *"The only high-wattage heating appliance plugged in was the microwave."*

#### Case A (Adversarial Distractor)
- **S3**: *"The television consumes very little electricity when in standby mode."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.1057 | 0.9383 | -0.0440 |
| BERT Similarity | 0.3377 | 0.4065 | 0.2558 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The high-wattage heating appliance that caused the blackout was in the kitchen."`
- **S2 Only**: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
- **S3 Only**: `"The context does not provide information about a blackout or which appliance caused it."`
- **S1, S2**:
  - `[S1, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S2, S1]`: `"The microwave caused the blackout.  The electrical failure was triggered by the microwave, a high-wattage heating appliance."`
- **S1, S3**:
  - `[S1, S3]`: `"The high-wattage heating appliance in the kitchen caused the blackout."`
  - `[S3, S1]`: `"The blackout was caused by a high-wattage heating appliance."`
- **S2, S3**:
  - `[S2, S3]`: `"The microwave caused the blackout because it is the only high-wattage heating appliance plugged in."`
  - `[S3, S2]`: `"The microwave caused the blackout because it is the only high-wattage heating appliance plugged in."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S1, S3, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S2, S1, S3]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in when the electrical failure occurred."`
  - `[S2, S3, S1]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S3, S1, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S3, S2, S1]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`

#### Case B (Syntactic Distractor)
- **S3**: *"The microwave destroyed the ceramic bowl."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0017 | 0.4752 | 0.5230 |
| BERT Similarity | 0.3570 | 0.4577 | 0.1853 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The high-wattage heating appliance that caused the blackout was in the kitchen."`
- **S2 Only**: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
- **S3 Only**: `"The context does not provide information about a blackout."`
- **S1, S2**:
  - `[S1, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S2, S1]`: `"The microwave caused the blackout.  The electrical failure was triggered by the microwave, a high-wattage heating appliance."`
- **S1, S3**:
  - `[S1, S3]`: `"The high-wattage heating appliance that caused the blackout was the microwave."`
  - `[S3, S1]`: `"The electrical failure was triggered by a high-wattage heating appliance, which was likely the microwave."`
- **S2, S3**:
  - `[S2, S3]`: `"The microwave caused the blackout because it was the only high-wattage heating appliance plugged in."`
  - `[S3, S2]`: `"The microwave caused the blackout because it was the only high-wattage heating appliance plugged in."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S1, S3, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S2, S1, S3]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in and its failure triggered the electrical issue."`
  - `[S2, S3, S1]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in and its electrical failure triggered the outage."`
  - `[S3, S1, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in when the electrical failure occurred."`
  - `[S3, S2, S1]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in when the electrical failure occurred."`

#### Case C (Semantic Distractor)
- **S3**: *"The massive power loss was initiated when someone turned on the high-wattage kitchen heating appliance."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.0165 | 0.9269 | 0.0896 |
| BERT Similarity | 0.3032 | 0.3940 | 0.3028 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The high-wattage heating appliance that caused the blackout was in the kitchen."`
- **S2 Only**: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
- **S3 Only**: `"The high-wattage kitchen heating appliance caused the blackout."`
- **S1, S2**:
  - `[S1, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S2, S1]`: `"The microwave caused the blackout.  The electrical failure was triggered by the microwave, a high-wattage heating appliance."`
- **S1, S3**:
  - `[S1, S3]`: `"The high-wattage kitchen heating appliance caused the blackout.  Someone turned it on, initiating the massive power loss."`
  - `[S3, S1]`: `"The high-wattage kitchen heating appliance caused the blackout."`
- **S2, S3**:
  - `[S2, S3]`: `"The microwave caused the blackout.  Someone turned on the microwave, which is a high-wattage heating appliance, initiating the power loss."`
  - `[S3, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The microwave caused the blackout.  Someone turned on the microwave, which is a high-wattage heating appliance."`
  - `[S1, S3, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S2, S1, S3]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in and its activation triggered the electrical failure."`
  - `[S2, S3, S1]`: `"The microwave caused the blackout.  Someone turned on the microwave, which overloaded the electrical system."`
  - `[S3, S1, S2]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`
  - `[S3, S2, S1]`: `"The microwave caused the blackout.  It was the only high-wattage heating appliance plugged in."`

---

### Weapon / Armor (Example 5) — 5/5 checks passed ✅ (Good)
**Quality score**: 0.2075

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.4067 >= best(S1,S2)=0.4964 - 0.15
- ✅ Case B BERT not fooled: S3=0.1295 <= worst(S1,S2)=0.3867 + 0.15
- ✅ Case C BERT fooled: S3=0.3706 >= best(S1,S2)=0.3303 - 0.15
- ✅ Case C ULL not fooled: S3=0.1027 <= worst(S1,S2)=0.1024 + 0.15

- **Q**: *"Which weapon pierced the knight's armor?"*
- **R**: *"The crossbow pierced the knight's armor."*
- **S1**: *"The metal plating was punctured by a ranged firing mechanism."*
- **S2**: *"The only ranged firing mechanism on the battlefield was the crossbow."*

#### Case A (Adversarial Distractor)
- **S3**: *"The dull training sword is completely harmless in real combat."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.1817 | 0.8174 | 0.0009 |
| BERT Similarity | 0.3809 | 0.4913 | 0.1278 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"A ranged firing mechanism pierced the knight's armor."`
- **S2 Only**: `"The crossbow pierced the knight's armor."`
- **S3 Only**: `"The context does not provide information about a knight or a weapon piercing their armor."`
- **S1, S2**:
  - `[S1, S2]`: `"The crossbow pierced the knight's armor."`
  - `[S2, S1]`: `"The crossbow pierced the knight's armor."`
- **S1, S3**:
  - `[S1, S3]`: `"A ranged firing mechanism pierced the knight's armor."`
  - `[S3, S1]`: `"A ranged firing mechanism pierced the knight's armor."`
- **S2, S3**:
  - `[S2, S3]`: `"The crossbow pierced the knight's armor."`
  - `[S3, S2]`: `"The context does not state which weapon pierced the knight's armor.  It only mentions a training sword and a crossbow."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The crossbow pierced the knight's armor."`
  - `[S1, S3, S2]`: `"The crossbow pierced the knight's armor."`
  - `[S2, S1, S3]`: `"The crossbow pierced the knight's armor."`
  - `[S2, S3, S1]`: `"The crossbow pierced the knight's armor."`
  - `[S3, S1, S2]`: `"The crossbow pierced the knight's armor."`
  - `[S3, S2, S1]`: `"The metal plating was punctured by a ranged firing mechanism, which was the crossbow."`

#### Case B (Syntactic Distractor)
- **S3**: *"The crossbow pierced the wooden target."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0968 | 0.4964 | 0.4067 |
| BERT Similarity | 0.3867 | 0.4838 | 0.1295 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"A ranged firing mechanism pierced the knight's armor."`
- **S2 Only**: `"The crossbow pierced the knight's armor."`
- **S3 Only**: `"The context does not say which weapon pierced the knight's armor.  It only says that a crossbow pierced a wooden target."`
- **S1, S2**:
  - `[S1, S2]`: `"The crossbow pierced the knight's armor."`
  - `[S2, S1]`: `"The crossbow pierced the knight's armor."`
- **S1, S3**:
  - `[S1, S3]`: `"A ranged firing mechanism, specifically a crossbow, pierced the knight's armor."`
  - `[S3, S1]`: `"A ranged firing mechanism, likely a crossbow, pierced the knight's armor."`
- **S2, S3**:
  - `[S2, S3]`: `"The crossbow pierced the wooden target, so it is likely the weapon that pierced the knight's armor."`
  - `[S3, S2]`: `"The crossbow pierced the knight's armor because it was the only ranged firing mechanism on the battlefield."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The crossbow pierced the knight's armor."`
  - `[S1, S3, S2]`: `"The crossbow pierced the knight's armor.  It was the only ranged firing mechanism on the battlefield."`
  - `[S2, S1, S3]`: `"The crossbow pierced the knight's armor."`
  - `[S2, S3, S1]`: `"The crossbow pierced the knight's armor."`
  - `[S3, S1, S2]`: `"The crossbow pierced the knight's armor.  It was the only ranged firing mechanism on the battlefield."`
  - `[S3, S2, S1]`: `"The crossbow pierced the knight's armor.  It was the only ranged firing mechanism on the battlefield."`

#### Case C (Semantic Distractor)
- **S3**: *"A mechanical bolt-launching weapon pierced the knight's armor during the battle."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.1024 | 0.7949 | 0.1027 |
| BERT Similarity | 0.2991 | 0.3303 | 0.3706 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"A ranged firing mechanism pierced the knight's armor."`
- **S2 Only**: `"The crossbow pierced the knight's armor."`
- **S3 Only**: `"A mechanical bolt-launching weapon pierced the knight's armor."`
- **S1, S2**:
  - `[S1, S2]`: `"The crossbow pierced the knight's armor."`
  - `[S2, S1]`: `"The crossbow pierced the knight's armor."`
- **S1, S3**:
  - `[S1, S3]`: `"A mechanical bolt-launching weapon pierced the knight's armor during the battle."`
  - `[S3, S1]`: `"A mechanical bolt-launching weapon pierced the knight's armor."`
- **S2, S3**:
  - `[S2, S3]`: `"A mechanical bolt-launching weapon, likely a crossbow, pierced the knight's armor."`
  - `[S3, S2]`: `"A mechanical bolt-launching weapon, which was a crossbow, pierced the knight's armor."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"A mechanical bolt-launching weapon, the crossbow, pierced the knight's armor."`
  - `[S1, S3, S2]`: `"A mechanical bolt-launching weapon, specifically a crossbow, pierced the knight's armor."`
  - `[S2, S1, S3]`: `"A mechanical bolt-launching weapon, likely a crossbow, pierced the knight's armor."`
  - `[S2, S3, S1]`: `"A mechanical bolt-launching weapon, the crossbow, pierced the knight's armor."`
  - `[S3, S1, S2]`: `"A crossbow pierced the knight's armor during the battle."`
  - `[S3, S2, S1]`: `"The crossbow pierced the knight's armor during the battle."`

---

### History / Document (Example 6) — 5/5 checks passed ✅ (Good)
**Quality score**: -0.1934

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.5680 >= best(S1,S2)=0.5857 - 0.15
- ✅ Case B BERT not fooled: S3=0.3469 <= worst(S1,S2)=0.3178 + 0.15
- ✅ Case C BERT fooled: S3=0.2953 >= best(S1,S2)=0.3899 - 0.15
- ✅ Case C ULL not fooled: S3=-0.0963 <= worst(S1,S2)=-0.1483 + 0.15

- **Q**: *"Which document established the peace treaty?"*
- **R**: *"The Treaty of Utrecht established the peace treaty."*
- **S1**: *"The peace agreement was settled by the pact signed in the year 1713."*
- **S2**: *"The only pact signed in the year 1713 to end the war was the Treaty of Utrecht."*

#### Case A (Adversarial Distractor)
- **S3**: *"The Magna Carta was signed in 1215 to limit the power of the king."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0223 | 1.5464 | -0.5686 |
| BERT Similarity | 0.3527 | 0.4325 | 0.2148 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The peace treaty was established by the pact signed in the year 1713."`
- **S2 Only**: `"The Treaty of Utrecht established the peace treaty."`
- **S3 Only**: `"The provided context does not mention a peace treaty."`
- **S1, S2**:
  - `[S1, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
  - `[S2, S1]`: `"The Treaty of Utrecht established the peace treaty."`
- **S1, S3**:
  - `[S1, S3]`: `"The peace treaty was established by the pact signed in the year 1713."`
  - `[S3, S1]`: `"The peace agreement was established by the pact signed in the year 1713."`
- **S2, S3**:
  - `[S2, S3]`: `"The Treaty of Utrecht established the peace treaty.  It was signed in 1713 to end the war."`
  - `[S3, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was signed in 1713 to end the war."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The peace treaty was established by the Treaty of Utrecht.  It was signed in 1713 to end the war."`
  - `[S1, S3, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
  - `[S2, S1, S3]`: `"The Treaty of Utrecht established the peace treaty.  The peace agreement was settled by the pact signed in 1713."`
  - `[S2, S3, S1]`: `"The peace treaty was established by the Treaty of Utrecht, signed in 1713."`
  - `[S3, S1, S2]`: `"The peace treaty was established by the Treaty of Utrecht.  It was signed in 1713 to end the war."`
  - `[S3, S2, S1]`: `"The peace agreement was settled by the Treaty of Utrecht, signed in 1713."`

#### Case B (Syntactic Distractor)
- **S3**: *"The Treaty of Utrecht redrew the map of Europe."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.1537 | 0.5857 | 0.5680 |
| BERT Similarity | 0.3178 | 0.3353 | 0.3469 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The peace treaty was established by the pact signed in the year 1713."`
- **S2 Only**: `"The Treaty of Utrecht established the peace treaty."`
- **S3 Only**: `"The Treaty of Utrecht established the peace treaty."`
- **S1, S2**:
  - `[S1, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
  - `[S2, S1]`: `"The Treaty of Utrecht established the peace treaty."`
- **S1, S3**:
  - `[S1, S3]`: `"The peace treaty was established by the pact signed in 1713.  The Treaty of Utrecht is the name of the document that established the peace."`
  - `[S3, S1]`: `"The peace treaty was established by the pact signed in 1713.  This pact is known as the Treaty of Utrecht."`
- **S2, S3**:
  - `[S2, S3]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
  - `[S3, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The peace treaty was established by the Treaty of Utrecht.  The Treaty of Utrecht was signed in 1713 to end the war."`
  - `[S1, S3, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
  - `[S2, S1, S3]`: `"The Treaty of Utrecht established the peace treaty.  The peace agreement was settled by the pact signed in 1713."`
  - `[S2, S3, S1]`: `"The peace treaty was established by the Treaty of Utrecht, signed in 1713."`
  - `[S3, S1, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
  - `[S3, S2, S1]`: `"The Treaty of Utrecht established the peace treaty.  The peace agreement was settled by the pact signed in the year 1713."`

#### Case C (Semantic Distractor)
- **S3**: *"The international pact signed in 1713 resolved the war."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.1483 | 1.2445 | -0.0963 |
| BERT Similarity | 0.3149 | 0.3899 | 0.2953 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The peace treaty was established by the pact signed in the year 1713."`
- **S2 Only**: `"The Treaty of Utrecht established the peace treaty."`
- **S3 Only**: `"The international pact signed in 1713 established the peace treaty."`
- **S1, S2**:
  - `[S1, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
  - `[S2, S1]`: `"The Treaty of Utrecht established the peace treaty."`
- **S1, S3**:
  - `[S1, S3]`: `"The peace treaty was established by the international pact signed in 1713."`
  - `[S3, S1]`: `"The international pact signed in 1713 established the peace treaty.  The peace agreement was settled by this pact."`
- **S2, S3**:
  - `[S2, S3]`: `"The Treaty of Utrecht established the peace treaty.  The international pact signed in 1713 resolved the war."`
  - `[S3, S2]`: `"The Treaty of Utrecht established the peace treaty.  It was the only pact signed in 1713 to end the war."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The peace treaty was established by the Treaty of Utrecht."`
  - `[S1, S3, S2]`: `"The peace treaty was established by the Treaty of Utrecht.  The Treaty of Utrecht was the only pact signed in 1713 to end the war."`
  - `[S2, S1, S3]`: `"The Treaty of Utrecht established the peace treaty."`
  - `[S2, S3, S1]`: `"The Treaty of Utrecht established the peace treaty."`
  - `[S3, S1, S2]`: `"The Treaty of Utrecht established the peace treaty."`
  - `[S3, S2, S1]`: `"The peace treaty was established by the Treaty of Utrecht."`

---

### Aviation / Incident (Example 7) — 5/5 checks passed ✅ (Good)
**Quality score**: -0.1452

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.5903 >= best(S1,S2)=0.5056 - 0.15
- ✅ Case B BERT not fooled: S3=0.4101 <= worst(S1,S2)=0.2631 + 0.15
- ✅ Case C BERT fooled: S3=0.3312 >= best(S1,S2)=0.3633 - 0.15
- ✅ Case C ULL not fooled: S3=-0.0374 <= worst(S1,S2)=-0.0882 + 0.15

- **Q**: *"Which aircraft caused the runway collision?"*
- **R**: *"Flight Alpha-9 caused the runway collision."*
- **S1**: *"The airport accident was triggered by a twin-engine commercial jetliner."*
- **S2**: *"The only twin-engine commercial jetliner taxiing at that time was Flight Alpha-9."*

#### Case A (Adversarial Distractor)
- **S3**: *"Helicopters require a landing pad and can hover in place."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.0732 | 1.2957 | -0.2225 |
| BERT Similarity | 0.4024 | 0.4213 | 0.1763 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The twin-engine commercial jetliner caused the runway collision."`
- **S2 Only**: `"Flight Alpha-9, the only twin-engine commercial jetliner taxiing, caused the runway collision."`
- **S3 Only**: `"The context does not provide information about a runway collision or the type of aircraft involved."`
- **S1, S2**:
  - `[S1, S2]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision."`
  - `[S2, S1]`: `"The twin-engine commercial jetliner taxiing at the time, Flight Alpha-9, caused the runway collision."`
- **S1, S3**:
  - `[S1, S3]`: `"The twin-engine commercial jetliner caused the runway collision.  Helicopters require a landing pad and can hover in place."`
  - `[S3, S1]`: `"The runway collision was caused by a twin-engine commercial jetliner."`
- **S2, S3**:
  - `[S2, S3]`: `"The runway collision was caused by Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time."`
  - `[S3, S2]`: `"The context states that Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time.  Therefore, Flight Alpha-9 caused the runway collision."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The twin-engine commercial jetliner, Flight Alpha-9, caused the runway collision."`
  - `[S1, S3, S2]`: `"The twin-engine commercial jetliner, Flight Alpha-9, caused the runway collision."`
  - `[S2, S1, S3]`: `"The twin-engine commercial jetliner, Flight Alpha-9, caused the runway collision."`
  - `[S2, S3, S1]`: `"The runway collision was caused by Flight Alpha-9, a twin-engine commercial jetliner."`
  - `[S3, S1, S2]`: `"The runway collision was caused by Flight Alpha-9, a twin-engine commercial jetliner."`
  - `[S3, S2, S1]`: `"The airport accident was triggered by Flight Alpha-9, a twin-engine commercial jetliner."`

#### Case B (Syntactic Distractor)
- **S3**: *"Flight Alpha-9 caused a minor runway collision during a simulator test."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.0959 | 0.5056 | 0.5903 |
| BERT Similarity | 0.2631 | 0.3268 | 0.4101 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The twin-engine commercial jetliner caused the runway collision."`
- **S2 Only**: `"Flight Alpha-9, the only twin-engine commercial jetliner taxiing, caused the runway collision."`
- **S3 Only**: `"Flight Alpha-9 caused the runway collision during a simulator test."`
- **S1, S2**:
  - `[S1, S2]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision."`
  - `[S2, S1]`: `"The twin-engine commercial jetliner taxiing at the time, Flight Alpha-9, caused the runway collision."`
- **S1, S3**:
  - `[S1, S3]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test."`
  - `[S3, S1]`: `"Flight Alpha-9 caused the runway collision during a simulator test."`
- **S2, S3**:
  - `[S2, S3]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test."`
  - `[S3, S2]`: `"Flight Alpha-9 caused the runway collision during a simulator test."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test."`
  - `[S1, S3, S2]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision during a simulator test."`
  - `[S2, S1, S3]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test."`
  - `[S2, S3, S1]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test."`
  - `[S3, S1, S2]`: `"Flight Alpha-9 caused the runway collision during a simulator test."`
  - `[S3, S2, S1]`: `"Flight Alpha-9 caused the runway collision."`

#### Case C (Semantic Distractor)
- **S3**: *"A twin-engine commercial jetliner caused the runway collision."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.0882 | 1.1256 | -0.0374 |
| BERT Similarity | 0.3055 | 0.3633 | 0.3312 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The twin-engine commercial jetliner caused the runway collision."`
- **S2 Only**: `"Flight Alpha-9, the only twin-engine commercial jetliner taxiing, caused the runway collision."`
- **S3 Only**: `"A twin-engine commercial jetliner caused the runway collision."`
- **S1, S2**:
  - `[S1, S2]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision."`
  - `[S2, S1]`: `"The twin-engine commercial jetliner taxiing at the time, Flight Alpha-9, caused the runway collision."`
- **S1, S3**:
  - `[S1, S3]`: `"A twin-engine commercial jetliner caused the runway collision."`
  - `[S3, S1]`: `"A twin-engine commercial jetliner caused the runway collision."`
- **S2, S3**:
  - `[S2, S3]`: `"Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time, caused the runway collision."`
  - `[S3, S2]`: `"Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time, caused the runway collision."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"A twin-engine commercial jetliner caused the runway collision.  Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time."`
  - `[S1, S3, S2]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision."`
  - `[S2, S1, S3]`: `"A twin-engine commercial jetliner caused the runway collision.  Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time."`
  - `[S2, S3, S1]`: `"A twin-engine commercial jetliner caused the runway collision.  Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time."`
  - `[S3, S1, S2]`: `"Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision."`
  - `[S3, S2, S1]`: `"Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time, caused the runway collision."`

---

### Astronomy / Telescope (Example 8) — 5/5 checks passed ✅ (Good)
**Quality score**: -0.0839

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.5196 >= best(S1,S2)=0.4853 - 0.15
- ✅ Case B BERT not fooled: S3=0.3057 <= worst(S1,S2)=0.2982 + 0.15
- ✅ Case C BERT fooled: S3=0.3050 >= best(S1,S2)=0.3965 - 0.15
- ✅ Case C ULL not fooled: S3=-0.0115 <= worst(S1,S2)=-0.0307 + 0.15

- **Q**: *"Which instrument discovered the distant exoplanet?"*
- **R**: *"The Kepler satellite discovered the exoplanet."*
- **S1**: *"The exoplanet was detected by a space-based transit-photometry telescope."*
- **S2**: *"The only space-based transit-photometry telescope active during the mission was the Kepler satellite."*

#### Case A (Adversarial Distractor)
- **S3**: *"Radio telescopes on Earth detect emissions from distant pulsars and quasars."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0525 | 1.1262 | -0.1787 |
| BERT Similarity | 0.2995 | 0.4996 | 0.2008 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The exoplanet was discovered by a space-based transit-photometry telescope."`
- **S2 Only**: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to observe the planet."`
- **S3 Only**: `"The context does not state which instrument discovered a distant exoplanet.  It only mentions radio telescopes used to detect emissions from pulsars and quasars."`
- **S1, S2**:
  - `[S1, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet."`
  - `[S2, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It was the only space-based transit-photometry telescope active during the mission."`
- **S1, S3**:
  - `[S1, S3]`: `"A space-based transit-photometry telescope discovered the distant exoplanet.  Radio telescopes are used to detect emissions from pulsars and quasars."`
  - `[S3, S1]`: `"The exoplanet was discovered by a space-based transit-photometry telescope.  Radio telescopes on Earth are used to detect emissions from pulsars and quasars."`
- **S2, S3**:
  - `[S2, S3]`: `"The Kepler satellite discovered the distant exoplanet.  It is a space-based transit-photometry telescope."`
  - `[S3, S2]`: `"The Kepler satellite, a space-based transit-photometry telescope, discovered the distant exoplanet."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet."`
  - `[S1, S3, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet."`
  - `[S2, S1, S3]`: `"The exoplanet was discovered by a space-based transit-photometry telescope.  The Kepler satellite was the only space-based transit-photometry telescope active during the mission."`
  - `[S2, S3, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It is the only space-based transit-photometry telescope active during the mission."`
  - `[S3, S1, S2]`: `"The exoplanet was discovered by the Kepler satellite.  It is a space-based transit-photometry telescope."`
  - `[S3, S2, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It was the only space-based transit-photometry telescope active during the mission."`

#### Case B (Syntactic Distractor)
- **S3**: *"The Kepler satellite was deactivated after its fuel supply ran out."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.0049 | 0.4853 | 0.5196 |
| BERT Similarity | 0.2982 | 0.3962 | 0.3057 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The exoplanet was discovered by a space-based transit-photometry telescope."`
- **S2 Only**: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to observe the planet."`
- **S3 Only**: `"The Kepler satellite discovered the distant exoplanet."`
- **S1, S2**:
  - `[S1, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet."`
  - `[S2, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It was the only space-based transit-photometry telescope active during the mission."`
- **S1, S3**:
  - `[S1, S3]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet."`
  - `[S3, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It was a space-based transit-photometry telescope."`
- **S2, S3**:
  - `[S2, S3]`: `"The Kepler satellite discovered the distant exoplanet.  It was the only space-based transit-photometry telescope active during the mission."`
  - `[S3, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It was the only space-based transit-photometry telescope active during the mission."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet."`
  - `[S1, S3, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It was the only active space-based transit-photometry telescope during the mission."`
  - `[S2, S1, S3]`: `"The exoplanet was discovered by the Kepler satellite.  It was the only space-based transit-photometry telescope active during the mission."`
  - `[S2, S3, S1]`: `"The exoplanet was discovered by the Kepler satellite."`
  - `[S3, S1, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It was the only active space-based transit-photometry telescope during the mission."`
  - `[S3, S2, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It was the only space-based transit-photometry telescope active during the mission."`

#### Case C (Semantic Distractor)
- **S3**: *"A space telescope measuring light dips detected the exoplanet."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.0307 | 1.0421 | -0.0115 |
| BERT Similarity | 0.2985 | 0.3965 | 0.3050 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The exoplanet was discovered by a space-based transit-photometry telescope."`
- **S2 Only**: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to observe the planet."`
- **S3 Only**: `"A space telescope discovered the distant exoplanet."`
- **S1, S2**:
  - `[S1, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet."`
  - `[S2, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It was the only space-based transit-photometry telescope active during the mission."`
- **S1, S3**:
  - `[S1, S3]`: `"The exoplanet was discovered by a space-based transit-photometry telescope."`
  - `[S3, S1]`: `"A space-based transit-photometry telescope discovered the distant exoplanet."`
- **S2, S3**:
  - `[S2, S3]`: `"The Kepler satellite, a space-based transit-photometry telescope, discovered the distant exoplanet."`
  - `[S3, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the light dips caused by the planet passing in front of its star."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The Kepler satellite discovered the distant exoplanet.  A space telescope measuring light dips detected the exoplanet."`
  - `[S1, S3, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It detected the exoplanet using space-based transit-photometry."`
  - `[S2, S1, S3]`: `"The exoplanet was discovered by the Kepler satellite.  It is the only space-based transit-photometry telescope active during the mission."`
  - `[S2, S3, S1]`: `"The exoplanet was discovered by a space-based transit-photometry telescope.  The Kepler satellite was the only space-based transit-photometry telescope active during the mission."`
  - `[S3, S1, S2]`: `"The Kepler satellite discovered the distant exoplanet.  It used transit-photometry to detect the planet by measuring dips in light."`
  - `[S3, S2, S1]`: `"The exoplanet was discovered by the Kepler satellite.  It is the only space-based transit-photometry telescope active during the mission."`

---

### Music / Era (Example 9) — 5/5 checks passed ✅ (Good)
**Quality score**: 0.0508

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.4042 >= best(S1,S2)=0.4730 - 0.15
- ✅ Case B BERT not fooled: S3=0.2230 <= worst(S1,S2)=0.3777 + 0.15
- ✅ Case C BERT fooled: S3=0.3366 >= best(S1,S2)=0.3938 - 0.15
- ✅ Case C ULL not fooled: S3=0.0640 <= worst(S1,S2)=0.0860 + 0.15

- **Q**: *"Which composer wrote the symphony?"*
- **R**: *"Ludwig van Beethoven wrote the symphony."*
- **S1**: *"The musical piece was composed by a deaf German master transitioning from Classical to Romantic."*
- **S2**: *"The only deaf German composer transitioning between those eras was Ludwig van Beethoven."*

#### Case A (Adversarial Distractor)
- **S3**: *"Wolfgang Amadeus Mozart was a prolific child prodigy of the Classical era."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.5360 | 1.0956 | -0.6316 |
| BERT Similarity | 0.4065 | 0.4794 | 0.1141 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The symphony was composed by a deaf German master."`
- **S2 Only**: `"Ludwig van Beethoven was the deaf German composer."`
- **S3 Only**: `"The context does not provide information about which composer wrote a symphony."`
- **S1, S2**:
  - `[S1, S2]`: `"Ludwig van Beethoven wrote the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S2, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`
- **S1, S3**:
  - `[S1, S3]`: `"The context states the composer was a deaf German master transitioning from Classical to Romantic."`
  - `[S3, S1]`: `"The symphony was composed by a deaf German master transitioning from Classical to Romantic."`
- **S2, S3**:
  - `[S2, S3]`: `"The context states that Ludwig van Beethoven was the only deaf German composer transitioning between eras.  Therefore, Beethoven wrote the symphony."`
  - `[S3, S2]`: `"The context does not provide information about which composer wrote a symphony."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"Ludwig van Beethoven wrote the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S1, S3, S2]`: `"The symphony was written by Ludwig van Beethoven.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S2, S1, S3]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`
  - `[S2, S3, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`
  - `[S3, S1, S2]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic music."`
  - `[S3, S2, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`

#### Case B (Syntactic Distractor)
- **S3**: *"Ludwig van Beethoven composed nine complete symphonies in his lifetime."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.1228 | 0.4730 | 0.4042 |
| BERT Similarity | 0.3777 | 0.3993 | 0.2230 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The symphony was composed by a deaf German master."`
- **S2 Only**: `"Ludwig van Beethoven was the deaf German composer."`
- **S3 Only**: `"Ludwig van Beethoven composed nine complete symphonies in his lifetime."`
- **S1, S2**:
  - `[S1, S2]`: `"Ludwig van Beethoven wrote the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S2, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`
- **S1, S3**:
  - `[S1, S3]`: `"Ludwig van Beethoven composed the symphony.  He was a deaf German master transitioning from Classical to Romantic music."`
  - `[S3, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`
- **S2, S3**:
  - `[S2, S3]`: `"Ludwig van Beethoven, a deaf German composer, wrote nine complete symphonies."`
  - `[S3, S2]`: `"Ludwig van Beethoven composed nine complete symphonies in his lifetime."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"Ludwig van Beethoven wrote the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S1, S3, S2]`: `"Ludwig van Beethoven composed the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S2, S1, S3]`: `"Ludwig van Beethoven composed the symphony.  He was a deaf German master transitioning from Classical to Romantic."`
  - `[S2, S3, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`
  - `[S3, S1, S2]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic music."`
  - `[S3, S2, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`

#### Case C (Semantic Distractor)
- **S3**: *"A deaf German composer transitioning from Classical to Romantic wrote the symphony."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | 0.0860 | 0.8500 | 0.0640 |
| BERT Similarity | 0.2696 | 0.3938 | 0.3366 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer the question."`
- **S1 Only**: `"The symphony was composed by a deaf German master."`
- **S2 Only**: `"Ludwig van Beethoven was the deaf German composer."`
- **S3 Only**: `"The symphony was written by a deaf German composer."`
- **S1, S2**:
  - `[S1, S2]`: `"Ludwig van Beethoven wrote the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S2, S1]`: `"The symphony was composed by Ludwig van Beethoven.  He was a deaf German master transitioning from Classical to Romantic."`
- **S1, S3**:
  - `[S1, S3]`: `"A deaf German composer transitioning from Classical to Romantic wrote the symphony."`
  - `[S3, S1]`: `"The symphony was written by a deaf German composer."`
- **S2, S3**:
  - `[S2, S3]`: `"Ludwig van Beethoven wrote the symphony.  He was a deaf German composer transitioning from Classical to Romantic."`
  - `[S3, S2]`: `"Ludwig van Beethoven wrote the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"Ludwig van Beethoven wrote the symphony."`
  - `[S1, S3, S2]`: `"Ludwig van Beethoven wrote the symphony."`
  - `[S2, S1, S3]`: `"The symphony was written by Ludwig van Beethoven.  He was a deaf German composer transitioning from Classical to Romantic."`
  - `[S2, S3, S1]`: `"The symphony was written by Ludwig van Beethoven.  He was a deaf German composer transitioning from Classical to Romantic."`
  - `[S3, S1, S2]`: `"Ludwig van Beethoven wrote the symphony.  He was the only deaf German composer transitioning from Classical to Romantic music."`
  - `[S3, S2, S1]`: `"The symphony was written by Ludwig van Beethoven.  He was the only deaf German composer transitioning between the Classical and Romantic eras."`

---

### Sociology / Theory (Example 10) — 5/5 checks passed ✅ (Good)
**Quality score**: 0.4093

**Diagnostic checks:**
- ✅ All values within [-1.5, 1.5]
- ✅ Case B ULL fooled: S3=0.7362 >= best(S1,S2)=0.4083 - 0.15
- ✅ Case B BERT not fooled: S3=0.3138 <= worst(S1,S2)=0.3284 + 0.15
- ✅ Case C BERT fooled: S3=0.3261 >= best(S1,S2)=0.3478 - 0.15
- ✅ Case C ULL not fooled: S3=-0.2507 <= worst(S1,S2)=-0.1622 + 0.15

- **Q**: *"Which sociological concept explained the rapid spread of the rumor?"*
- **R**: *"The contagion theory explained the rumor's spread."*
- **S1**: *"The collective behavior was explained by a framework stating that crowd emotions are highly infectious and spread rapidly."*
- **S2**: *"The only framework stating that crowd emotions are highly infectious and spread rapidly is the contagion theory."*

#### Case A (Adversarial Distractor)
- **S3**: *"The bystander effect describes how individuals are less likely to offer help when other people are present."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.2022 | 3.1609 | -1.9586 |
| BERT Similarity | 0.3794 | 0.4072 | 0.2133 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor."`
- **S2 Only**: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
- **S3 Only**: `"The provided context does not mention a rumor or explain its spread."`
- **S1, S2**:
  - `[S1, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S2, S1]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
- **S1, S3**:
  - `[S1, S3]`: `"The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor."`
  - `[S3, S1]`: `"The sociological concept that explained the rapid spread of the rumor is the idea that crowd emotions are highly infectious and spread rapidly."`
- **S2, S3**:
  - `[S2, S3]`: `"The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious."`
  - `[S3, S2]`: `"The sociological concept that explained the rapid spread of the rumor is the contagion theory.  This theory states that crowd emotions are highly infectious and spread rapidly."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious and spread rapidly."`
  - `[S1, S3, S2]`: `"The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious and spread rapidly."`
  - `[S2, S1, S3]`: `"The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious."`
  - `[S2, S3, S1]`: `"The sociological concept that explained the rapid spread of the rumor is the contagion theory.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S1, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S2, S1]`: `"The sociological concept that explained the rapid spread of the rumor is the contagion theory.  This theory posits that crowd emotions are highly infectious and spread rapidly."`

#### Case B (Syntactic Distractor)
- **S3**: *"The contagion theory was first proposed in the context of nineteenth-century crowd psychology."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.1444 | 0.4083 | 0.7362 |
| BERT Similarity | 0.3284 | 0.3578 | 0.3138 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor."`
- **S2 Only**: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
- **S3 Only**: `"The contagion theory, first proposed in the context of nineteenth-century crowd psychology, explains the rapid spread of the rumor."`
- **S1, S2**:
  - `[S1, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S2, S1]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
- **S1, S3**:
  - `[S1, S3]`: `"The sociological concept of contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S1]`: `"The contagion theory, which posits that crowd emotions are highly infectious and spread rapidly, explained the rumor's quick dissemination."`
- **S2, S3**:
  - `[S2, S3]`: `"The contagion theory, which posits that crowd emotions are highly infectious and spread rapidly, explains the rumor's quick dissemination."`
  - `[S3, S2]`: `"The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious and spread rapidly."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S1, S3, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S2, S1, S3]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S2, S3, S1]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S1, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S2, S1]`: `"The contagion theory explained the rapid spread of the rumor.  This theory states that crowd emotions are highly infectious and spread quickly."`

#### Case C (Semantic Distractor)
- **S3**: *"A framework stating that crowd emotions are highly infectious and spread rapidly explained the collective behavior."*

| Method | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: |
| Unweighted LL | -0.1622 | 1.4129 | -0.2507 |
| BERT Similarity | 0.3261 | 0.3478 | 0.3261 |

##### Generated Responses per Coalition:
- **Empty**: `"Please provide the context so I can answer your question."`
- **S1 Only**: `"The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor."`
- **S2 Only**: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
- **S3 Only**: `"The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor."`
- **S1, S2**:
  - `[S1, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S2, S1]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
- **S1, S3**:
  - `[S1, S3]`: `"The sociological concept that explained the rapid spread of the rumor is that crowd emotions are highly infectious and spread rapidly."`
  - `[S3, S1]`: `"The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor."`
- **S2, S3**:
  - `[S2, S3]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
- **S1, S2, S3**:
  - `[S1, S2, S3]`: `"The sociological concept that explained the rapid spread of the rumor is the contagion theory.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S1, S3, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S2, S1, S3]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S2, S3, S1]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S1, S2]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`
  - `[S3, S2, S1]`: `"The contagion theory explained the rapid spread of the rumor.  This theory posits that crowd emotions are highly infectious and spread quickly."`

---

