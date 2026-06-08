# Evaluation Report: Passed Examples

This file contains the detailed evaluation of the 11 verified context attribution examples. For each example, we compute the characteristic function values $v(S)$ for both Unweighted LL difference and BERT Similarity difference, display the generated model responses for all coalitions under BERT Similarity, and apply all 5 diagnostic rules.

## Overall Diagnostic Summary

| Example | Category | Passed All | Quality Score | Rule 1 (Extreme) | Rule 2 (B: ULL Fool) | Rule 3 (B: BERT Safe) | Rule 4 (C: BERT Fool) | Rule 5 (C: ULL Safe) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Chemistry / Lab Experiment | ✅ PASS | 0.4253 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2 | Mechanic / Car Part | ✅ PASS | -0.0588 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 3 | Medical / Gland | ✅ PASS | 0.1061 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 4 | Virology / Outbreak | ✅ PASS | -0.0292 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 5 | Ecology / Bloom | ✅ PASS | -0.1398 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 6 | Technology / Gadget | ✅ PASS | 0.0222 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 7 | Weapon / Armor | ✅ PASS | 0.2075 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 8 | Acoustics / Feedback | ✅ PASS | 0.0142 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 9 | History / Document | ✅ PASS | -0.1934 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 10 | Sports / Athlete | ✅ PASS | 0.1173 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 11 | Aviation / Incident | ✅ PASS | -0.1452 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 12 | Astronomy / Telescope | ✅ PASS | -0.0839 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 13 | Music / Era | ✅ PASS | 0.0508 | ✅ | ✅ | ✅ | ✅ | ✅ |
| 14 | Sociology / Theory | ✅ PASS | 0.4093 | ✅ | ✅ | ✅ | ✅ | ✅ |

---

## Detailed Evaluations per Example

### Example 1: Chemistry / Lab Experiment

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.4253`

#### Metadata
- **Question**: *"Which chemical caused the liquid to turn green?"*
- **Target Response**: *"Adding copper sulfate turned the liquid green."*
- **S1 (Logical premise 1)**: *"A substance containing copper was added to the mixture."*
- **S2 (Logical premise 2)**: *"The only copper compound present in the lab is copper sulfate."*
- **S3a (Adversarial Distractor)**: *"Cobalt chloride turns the mixture bright red."*
- **S3b (Syntactic Distractor)**: *"Copper sulfate is commonly used in agricultural fungicides to control mildew."*
- **S3c (Semantic Distractor)**: *"Cupric compounds are known to generate emerald-colored liquid solutions."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.2946 >= best(S1,S2)=0.3562 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.2552 <= worst(S1,S2)=0.2968 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3285 >= best(S1,S2)=0.3453 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.1666 <= worst(S1,S2)=0.2956 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Cobalt chloride turns the mixture bright red."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2149 |
| \{S1\} | 5.5156 | 0.7321 | 0.9470 |
| \{S2\} | 8.0781 | 0.6125 | 0.8274 |
| \{S3\} | 6.0391 | 0.5966 | 0.8114 |
| \{S1, S2\} | 10.8750 | 0.7851 | 1.0000 |
| \{S1, S3\} | 3.8320 | 0.6242 | 0.8391 |
| \{S2, S3\} | 7.4336 | 0.6096 | 0.8245 |
| \{S1, S2, S3\} | 10.4414 | 0.6902 | 0.9050 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The copper in the substance caused the liquid to turn green. <end_of_turn>" |
| (S2) | "The context does not say which chemical caused the liquid to turn green. <end_of_turn>" |
| (S3) | "The context does not provide information about a chemical that turned the liquid green. <end_of_turn>" |
| (S1, S2) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S2, S1) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S1, S3) | "The context does not say which chemical caused the liquid to turn green. It only states that copper and cobalt chloride affect the mixture's color. <end_of_turn>" |
| (S3, S1) | "The context does not say which chemical caused the liquid to turn green. <end_of_turn>" |
| (S2, S3) | "The context does not provide information about which chemical caused the liquid to turn green. <end_of_turn>" |
| (S3, S2) | "The context does not provide information about a chemical that turned the liquid green. <end_of_turn>" |
| (S1, S2, S3) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S1, S3, S2) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S2, S1, S3) | "The context does not state which chemical caused the liquid to turn green. <end_of_turn>" |
| (S2, S3, S1) | "The substance containing copper, copper sulfate, caused the liquid to turn green. <end_of_turn>" |
| (S3, S1, S2) | "The context does not state which chemical caused the liquid to turn green. <end_of_turn>" |
| (S3, S2, S1) | "The context does not say which chemical caused the liquid to turn green. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 2.9395 | 6.0215 | 1.4805 | 0.2815 | 0.5767 | 0.1418 |
| BERT Similarity | 0.3043 | 0.2372 | 0.1487 | 0.4409 | 0.3436 | 0.2155 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Copper sulfate is commonly used in agricultural fungicides to control mildew."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2889 |
| \{S1\} | 5.5156 | 0.6322 | 0.9211 |
| \{S2\} | 8.0781 | 0.5433 | 0.8322 |
| \{S3\} | 8.0938 | 0.4835 | 0.7723 |
| \{S1, S2\} | 10.8750 | 0.6500 | 0.9389 |
| \{S1, S3\} | 9.6250 | 0.6546 | 0.9434 |
| \{S2, S3\} | 7.2031 | 0.5429 | 0.8317 |
| \{S1, S2, S3\} | 10.0130 | 0.6641 | 0.9529 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The copper in the substance caused the liquid to turn green. <end_of_turn>" |
| (S2) | "The context does not say which chemical caused the liquid to turn green. <end_of_turn>" |
| (S3) | "The context does not provide information about a liquid turning green. <end_of_turn>" |
| (S1, S2) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S2, S1) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S1, S3) | "The copper sulfate added to the mixture caused the liquid to turn green. <end_of_turn>" |
| (S3, S1) | "The substance containing copper caused the liquid to turn green. <end_of_turn>" |
| (S2, S3) | "The context does not provide information about a liquid turning green. <end_of_turn>" |
| (S3, S2) | "Copper sulfate is the only copper compound present in the lab, so it caused the liquid to turn green. <end_of_turn>" |
| (S1, S2, S3) | "Copper sulfate, added to the mixture, caused the liquid to turn green. <end_of_turn>" |
| (S1, S3, S2) | "Copper sulfate, added to the mixture, caused the liquid to turn green. <end_of_turn>" |
| (S2, S1, S3) | "The substance containing copper, likely copper sulfate, caused the liquid to turn green. <end_of_turn>" |
| (S2, S3, S1) | "Copper sulfate, a copper compound, was added to the mixture and caused the liquid to turn green. <end_of_turn>" |
| (S3, S1, S2) | "Copper sulfate, the only copper compound present in the lab, caused the liquid to turn green. <end_of_turn>" |
| (S3, S2, S1) | "Copper sulfate, the only copper compound present in the lab, caused the liquid to turn green. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 3.4965 | 3.5668 | 2.9497 | 0.3492 | 0.3562 | 0.2946 |
| BERT Similarity | 0.2975 | 0.1971 | 0.1695 | 0.4479 | 0.2968 | 0.2552 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"Cupric compounds are known to generate emerald-colored liquid solutions."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2166 |
| \{S1\} | 5.5156 | 0.7072 | 0.9238 |
| \{S2\} | 8.0781 | 0.6197 | 0.8363 |
| \{S3\} | -2.1016 | 0.7063 | 0.9228 |
| \{S1, S2\} | 10.8750 | 0.7593 | 0.9759 |
| \{S1, S3\} | -1.2383 | 0.6473 | 0.8639 |
| \{S2, S3\} | 8.5625 | 0.7637 | 0.9802 |
| \{S1, S2, S3\} | 10.7422 | 0.7539 | 0.9705 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The copper in the substance caused the liquid to turn green. <end_of_turn>" |
| (S2) | "The context does not say which chemical caused the liquid to turn green. <end_of_turn>" |
| (S3) | "Cupric compounds caused the liquid to turn green. <end_of_turn>" |
| (S1, S2) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S2, S1) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S1, S3) | "The chemical that caused the liquid to turn green was the copper compound added to the mixture. Cupric compounds are known to create emerald-colored liquid solutions. <end_of_turn>" |
| (S3, S1) | "The substance containing copper caused the liquid to turn green. Cupric compounds are known to generate emerald-colored liquid solutions. <end_of_turn>" |
| (S2, S3) | "Copper sulfate, a copper compound, caused the liquid to turn green. <end_of_turn>" |
| (S3, S2) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S1, S2, S3) | "Copper sulfate, a cupric compound, caused the liquid to turn green. <end_of_turn>" |
| (S1, S3, S2) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |
| (S2, S1, S3) | "The substance containing copper, added to the mixture, caused the liquid to turn green. Cupric compounds are known to generate emerald-colored liquid solutions. <end_of_turn>" |
| (S2, S3, S1) | "Copper sulfate, a cupric compound, caused the liquid to turn green. <end_of_turn>" |
| (S3, S1, S2) | "Copper sulfate, a cupric compound, caused the liquid to turn green. <end_of_turn>" |
| (S3, S2, S1) | "Copper sulfate, the only copper compound present, caused the liquid to turn green. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 3.1751 | 9.3568 | -1.7897 | 0.2956 | 0.8710 | -0.1666 |
| BERT Similarity | 0.2459 | 0.2604 | 0.2476 | 0.3262 | 0.3453 | 0.3285 |

---

### Example 2: Mechanic / Car Part

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `-0.0588`

#### Metadata
- **Question**: *"Which part caused the engine to stall?"*
- **Target Response**: *"The carburetor caused the engine to stall."*
- **S1 (Logical premise 1)**: *"The mechanical failure was triggered by a fuel-air mixing component."*
- **S2 (Logical premise 2)**: *"The only fuel-air mixing component in the engine is the carburetor."*
- **S3a (Adversarial Distractor)**: *"The alternator is responsible for charging the battery while driving."*
- **S3b (Syntactic Distractor)**: *"The carburetor caused the exhaust to backfire."*
- **S3c (Semantic Distractor)**: *"The vehicle's motor abruptly stopped running because of a malfunction in the primary fuel-air mixing component."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.4034 >= best(S1,S2)=0.4986 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.2575 <= worst(S1,S2)=0.3694 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3275 >= best(S1,S2)=0.3768 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=0.0811 <= worst(S1,S2)=0.0549 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"The alternator is responsible for charging the battery while driving."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2496 |
| \{S1\} | 1.0938 | 0.6395 | 0.8892 |
| \{S2\} | 16.5859 | 0.6621 | 0.9117 |
| \{S3\} | -1.9297 | 0.4050 | 0.6546 |
| \{S1, S2\} | 22.9844 | 0.6825 | 0.9322 |
| \{S1, S3\} | 1.6445 | 0.6167 | 0.8664 |
| \{S2, S3\} | 10.9062 | 0.4050 | 0.6546 |
| \{S1, S2, S3\} | 22.7943 | 0.6913 | 0.9409 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The fuel-air mixing component caused the engine to stall. <end_of_turn>" |
| (S2) | "The carburetor, being the only fuel-air mixing component, likely caused the engine to stall. <end_of_turn>" |
| (S3) | "The context does not provide information about an engine stalling. <end_of_turn>" |
| (S1, S2) | "The carburetor caused the engine to stall. <end_of_turn>" |
| (S2, S1) | "The carburetor caused the engine to stall. The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine. <end_of_turn>" |
| (S1, S3) | "The fuel-air mixing component caused the engine to stall. <end_of_turn>" |
| (S3, S1) | "The engine stalled because of a mechanical failure in a fuel-air mixing component. <end_of_turn>" |
| (S2, S3) | "The context does not provide information about an engine stalling. <end_of_turn>" |
| (S3, S2) | "The context does not provide information about an engine stalling. <end_of_turn>" |
| (S1, S2, S3) | "The carburetor caused the engine to stall. It was the only fuel-air mixing component in the engine. <end_of_turn>" |
| (S1, S3, S2) | "The carburetor, the only fuel-air mixing component in the engine, caused the engine to stall. <end_of_turn>" |
| (S2, S1, S3) | "The carburetor caused the engine to stall. It experienced a mechanical failure. <end_of_turn>" |
| (S2, S3, S1) | "The carburetor, the only fuel-air mixing component, caused the engine to stall due to a mechanical failure. <end_of_turn>" |
| (S3, S1, S2) | "The carburetor caused the engine to stall. The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine. <end_of_turn>" |
| (S3, S2, S1) | "The carburetor, the only fuel-air mixing component in the engine, caused the mechanical failure and engine stall. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 5.9894 | 18.3663 | -1.5614 | 0.2628 | 0.8057 | -0.0685 |
| BERT Similarity | 0.3473 | 0.2527 | 0.0913 | 0.5024 | 0.3656 | 0.1320 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"The carburetor caused the exhaust to backfire."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.3650 |
| \{S1\} | 1.0938 | 0.5126 | 0.8776 |
| \{S2\} | 16.5859 | 0.5102 | 0.8752 |
| \{S3\} | 15.5781 | 0.4339 | 0.7989 |
| \{S1, S2\} | 22.9844 | 0.5768 | 0.9418 |
| \{S1, S3\} | 19.8047 | 0.5282 | 0.8931 |
| \{S2, S3\} | 21.9375 | 0.5263 | 0.8913 |
| \{S1, S2, S3\} | 22.0013 | 0.5583 | 0.9233 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The fuel-air mixing component caused the engine to stall. <end_of_turn>" |
| (S2) | "The carburetor, being the only fuel-air mixing component, likely caused the engine to stall. <end_of_turn>" |
| (S3) | "The context does not say which part caused the engine to stall. It only states that the carburetor caused the exhaust to backfire. <end_of_turn>" |
| (S1, S2) | "The carburetor caused the engine to stall. <end_of_turn>" |
| (S2, S1) | "The carburetor caused the engine to stall. The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine. <end_of_turn>" |
| (S1, S3) | "The fuel-air mixing component caused the engine to stall. <end_of_turn>" |
| (S3, S1) | "The carburetor, a fuel-air mixing component, caused the engine to stall. <end_of_turn>" |
| (S2, S3) | "The carburetor caused the engine to stall because it caused the exhaust to backfire. <end_of_turn>" |
| (S3, S2) | "The carburetor caused the engine to stall because it is the only fuel-air mixing component and its malfunction led to the engine backfiring. <end_of_turn>" |
| (S1, S2, S3) | "The carburetor caused the engine to stall. <end_of_turn>" |
| (S1, S3, S2) | "The carburetor caused the engine to stall because it led to a backfire in the exhaust. <end_of_turn>" |
| (S2, S1, S3) | "The carburetor caused the engine to stall because it experienced a mechanical failure. <end_of_turn>" |
| (S2, S3, S1) | "The carburetor caused the engine to stall because it was the fuel-air mixing component that experienced a mechanical failure. <end_of_turn>" |
| (S3, S1, S2) | "The carburetor caused the engine to stall because it was the fuel-air mixing component that failed. <end_of_turn>" |
| (S3, S2, S1) | "The carburetor caused the engine to stall because it was the fuel-air mixing component that experienced a mechanical failure. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 2.1567 | 10.9692 | 8.8754 | 0.0980 | 0.4986 | 0.4034 |
| BERT Similarity | 0.2084 | 0.2062 | 0.1437 | 0.3732 | 0.3694 | 0.2575 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"The vehicle's motor abruptly stopped running because of a malfunction in the primary fuel-air mixing component."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2886 |
| \{S1\} | 1.0938 | 0.6223 | 0.9110 |
| \{S2\} | 16.5859 | 0.6152 | 0.9039 |
| \{S3\} | 3.0938 | 0.5999 | 0.8886 |
| \{S1, S2\} | 22.9844 | 0.6480 | 0.9367 |
| \{S1, S3\} | 1.9727 | 0.5999 | 0.8886 |
| \{S2, S3\} | 22.1406 | 0.7114 | 1.0000 |
| \{S1, S2, S3\} | 22.0378 | 0.6425 | 0.9312 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The fuel-air mixing component caused the engine to stall. <end_of_turn>" |
| (S2) | "The carburetor, being the only fuel-air mixing component, likely caused the engine to stall. <end_of_turn>" |
| (S3) | "The engine stalled because of a malfunction in the primary fuel-air mixing component. <end_of_turn>" |
| (S1, S2) | "The carburetor caused the engine to stall. <end_of_turn>" |
| (S2, S1) | "The carburetor caused the engine to stall. The mechanical failure was triggered by the carburetor, which is the only fuel-air mixing component in the engine. <end_of_turn>" |
| (S1, S3) | "The engine stalled because of a malfunction in the primary fuel-air mixing component. <end_of_turn>" |
| (S3, S1) | "The engine stalled because of a malfunction in the primary fuel-air mixing component. <end_of_turn>" |
| (S2, S3) | "The malfunction in the carburetor caused the engine to stall. <end_of_turn>" |
| (S3, S2) | "The malfunction in the carburetor caused the engine to stall. <end_of_turn>" |
| (S1, S2, S3) | "The malfunction in the carburetor caused the engine to stall. <end_of_turn>" |
| (S1, S3, S2) | "The malfunction in the primary fuel-air mixing component caused the engine to stall. The carburetor is the only fuel-air mixing component in the engine. <end_of_turn>" |
| (S2, S1, S3) | "The carburetor, the only fuel-air mixing component in the engine, malfunctioned. This malfunction caused the vehicle's motor to abruptly stop running. <end_of_turn>" |
| (S2, S3, S1) | "The carburetor, the primary fuel-air mixing component, malfunctioned. This mechanical failure caused the engine to stall. <end_of_turn>" |
| (S3, S1, S2) | "The malfunction in the carburetor caused the engine to stall. <end_of_turn>" |
| (S3, S2, S1) | "The carburetor, the only fuel-air mixing component in the engine, malfunctioned. This mechanical failure caused the engine to stall. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 1.2099 | 19.0399 | 1.7880 | 0.0549 | 0.8640 | 0.0811 |
| BERT Similarity | 0.1900 | 0.2421 | 0.2104 | 0.2956 | 0.3768 | 0.3275 |

---

### Example 3: Medical / Gland

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.1061`

#### Metadata
- **Question**: *"Which compound caused the cell culture to mutate?"*
- **Target Response**: *"Adding peptide X-3 caused the cell culture to mutate."*
- **S1 (Logical premise 1)**: *"The mutation in the cell culture was triggered by a synthetic polymer."*
- **S2 (Logical premise 2)**: *"The only synthetic polymer in the incubator was peptide X-3."*
- **S3a (Adversarial Distractor)**: *"Peptide Y-5 is commonly used to inhibit bacterial growth."*
- **S3b (Syntactic Distractor)**: *"Peptide X-3 is stored in a sterilized glass vial."*
- **S3c (Semantic Distractor)**: *"An artificial organic compound initiated a genetic shift in the biological sample."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.5261 >= best(S1,S2)=0.5584 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.2350 <= worst(S1,S2)=0.3713 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.2805 >= best(S1,S2)=0.3658 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.1229 <= worst(S1,S2)=-0.0354 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Peptide Y-5 is commonly used to inhibit bacterial growth."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2077 |
| \{S1\} | -0.8594 | 0.5920 | 0.7997 |
| \{S2\} | 24.7969 | 0.6782 | 0.8859 |
| \{S3\} | 17.5547 | 0.4838 | 0.6915 |
| \{S1, S2\} | 22.8242 | 0.6841 | 0.8917 |
| \{S1, S3\} | 11.3555 | 0.6062 | 0.8139 |
| \{S2, S3\} | 24.7344 | 0.4554 | 0.6631 |
| \{S1, S2, S3\} | 22.3971 | 0.7419 | 0.9496 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The synthetic polymer caused the cell culture to mutate. <end_of_turn>" |
| (S2) | "The cell culture mutated due to exposure to peptide X-3. <end_of_turn>" |
| (S3) | "The context does not provide information about a cell culture mutating or which compound caused it. <end_of_turn>" |
| (S1, S2) | "Peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S2, S1) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S1, S3) | "The synthetic polymer caused the cell culture to mutate. Peptide Y-5 is not mentioned as the cause of the mutation. <end_of_turn>" |
| (S3, S1) | "A synthetic polymer, not Peptide Y-5, caused the cell culture to mutate. <end_of_turn>" |
| (S2, S3) | "The context does not provide information about which compound caused the cell culture to mutate. <end_of_turn>" |
| (S3, S2) | "The context does not provide information about cell culture mutations. <end_of_turn>" |
| (S1, S2, S3) | "The synthetic polymer peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S1, S3, S2) | "The synthetic polymer peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S2, S1, S3) | "The synthetic polymer that caused the cell culture to mutate was peptide X-3. <end_of_turn>" |
| (S2, S3, S1) | "The synthetic polymer that caused the cell culture to mutate was peptide X-3. <end_of_turn>" |
| (S3, S1, S2) | "The synthetic polymer peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S3, S2, S1) | "The mutation in the cell culture was triggered by the synthetic polymer peptide X-3. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -2.4275 | 17.0901 | 7.7346 | -0.1084 | 0.7630 | 0.3453 |
| BERT Similarity | 0.3142 | 0.2819 | 0.1458 | 0.4235 | 0.3800 | 0.1965 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Peptide X-3 is stored in a sterilized glass vial."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1919 |
| \{S1\} | -0.8594 | 0.6459 | 0.8378 |
| \{S2\} | 24.7969 | 0.6054 | 0.7973 |
| \{S3\} | 24.4844 | 0.4393 | 0.6312 |
| \{S1, S2\} | 22.8242 | 0.7306 | 0.9225 |
| \{S1, S3\} | 21.7148 | 0.7076 | 0.8995 |
| \{S2, S3\} | 24.3516 | 0.7171 | 0.9090 |
| \{S1, S2, S3\} | 22.0026 | 0.6938 | 0.8857 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The synthetic polymer caused the cell culture to mutate. <end_of_turn>" |
| (S2) | "The cell culture mutated due to exposure to peptide X-3. <end_of_turn>" |
| (S3) | "The context does not provide information about any cell culture or mutations. <end_of_turn>" |
| (S1, S2) | "Peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S2, S1) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S1, S3) | "A synthetic polymer caused the cell culture to mutate. Peptide X-3 is not the compound responsible. <end_of_turn>" |
| (S3, S1) | "A synthetic polymer, not Peptide X-3, caused the cell culture to mutate. <end_of_turn>" |
| (S2, S3) | "The context states that the only synthetic polymer in the incubator was peptide X-3. Therefore, peptide X-3 likely caused the cell culture to mutate. <end_of_turn>" |
| (S3, S2) | "The only synthetic polymer in the incubator was peptide X-3, so it caused the cell culture to mutate. <end_of_turn>" |
| (S1, S2, S3) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S1, S3, S2) | "The synthetic polymer peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S2, S1, S3) | "The mutation in the cell culture was triggered by the synthetic polymer peptide X-3. <end_of_turn>" |
| (S2, S3, S1) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S3, S1, S2) | "The synthetic polymer peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S3, S2, S1) | "The mutation in the cell culture was triggered by the synthetic polymer peptide X-3. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.8598 | 12.2867 | 11.5757 | -0.0845 | 0.5584 | 0.5261 |
| BERT Similarity | 0.2731 | 0.2576 | 0.1630 | 0.3937 | 0.3713 | 0.2350 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"An artificial organic compound initiated a genetic shift in the biological sample."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1919 |
| \{S1\} | -0.8594 | 0.6459 | 0.8378 |
| \{S2\} | 24.7969 | 0.6054 | 0.7973 |
| \{S3\} | -2.3672 | 0.5560 | 0.7479 |
| \{S1, S2\} | 22.8242 | 0.7306 | 0.9225 |
| \{S1, S3\} | -3.0234 | 0.6459 | 0.8378 |
| \{S2, S3\} | 20.7148 | 0.7055 | 0.8974 |
| \{S1, S2, S3\} | 20.6888 | 0.7859 | 0.9778 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The synthetic polymer caused the cell culture to mutate. <end_of_turn>" |
| (S2) | "The cell culture mutated due to exposure to peptide X-3. <end_of_turn>" |
| (S3) | "The artificial organic compound caused the cell culture to mutate. <end_of_turn>" |
| (S1, S2) | "Peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S2, S1) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S1, S3) | "The synthetic polymer caused the cell culture to mutate. <end_of_turn>" |
| (S3, S1) | "The synthetic polymer caused the cell culture to mutate. <end_of_turn>" |
| (S2, S3) | "Peptide X-3, the only synthetic polymer in the incubator, was the artificial organic compound that caused the genetic shift. <end_of_turn>" |
| (S3, S2) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S1, S2, S3) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S1, S3, S2) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S2, S1, S3) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S2, S3, S1) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |
| (S3, S1, S2) | "The synthetic polymer peptide X-3 caused the cell culture to mutate. <end_of_turn>" |
| (S3, S2, S1) | "Peptide X-3, the only synthetic polymer in the incubator, caused the cell culture to mutate. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.7333 | 23.9640 | -2.5419 | -0.0354 | 1.1583 | -0.1229 |
| BERT Similarity | 0.2780 | 0.2875 | 0.2205 | 0.3537 | 0.3658 | 0.2805 |

---

### Example 4: Virology / Outbreak

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `-0.0292`

#### Metadata
- **Question**: *"Which virus caused the outbreak in the village?"*
- **Target Response**: *"Strain H7-Alpha caused the outbreak in the village."*
- **S1 (Logical premise 1)**: *"The epidemic was traced to a highly mutagenic RNA pathogen."*
- **S2 (Logical premise 2)**: *"The only highly mutagenic RNA pathogen isolated from the patients was Strain H7-Alpha."*
- **S3a (Adversarial Distractor)**: *"Influenza vaccines are updated annually to match circulating strains."*
- **S3b (Syntactic Distractor)**: *"Strain H7-Alpha caused severe respiratory symptoms in laboratory primates."*
- **S3c (Semantic Distractor)**: *"A rapidly evolving ribonucleic acid microorganism sparked the community-wide contagion."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.4467 >= best(S1,S2)=0.5533 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.2999 <= worst(S1,S2)=0.2999 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3987 >= best(S1,S2)=0.3775 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.0619 <= worst(S1,S2)=-0.0057 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Influenza vaccines are updated annually to match circulating strains."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2184 |
| \{S1\} | -1.7734 | 0.5898 | 0.8082 |
| \{S2\} | 33.9219 | 0.7221 | 0.9406 |
| \{S3\} | -19.6562 | 0.5169 | 0.7353 |
| \{S1, S2\} | 36.4609 | 0.6722 | 0.8906 |
| \{S1, S3\} | -10.4219 | 0.6519 | 0.8703 |
| \{S2, S3\} | 35.1953 | 0.5998 | 0.8183 |
| \{S1, S2, S3\} | 33.8841 | 0.7126 | 0.9310 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The epidemic was caused by a highly mutagenic RNA pathogen. <end_of_turn>" |
| (S2) | "Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients. Therefore, it caused the outbreak in the village. <end_of_turn>" |
| (S3) | "The provided context does not mention a virus outbreak in a village. <end_of_turn>" |
| (S1, S2) | "The outbreak in the village was caused by Strain H7-Alpha. This virus was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S2, S1) | "The epidemic was caused by a highly mutagenic RNA pathogen. Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S1, S3) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. It is not specified what type of RNA pathogen caused the outbreak. <end_of_turn>" |
| (S3, S1) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. It was not influenza. <end_of_turn>" |
| (S2, S3) | "Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients. <end_of_turn>" |
| (S3, S2) | "The outbreak in the village was caused by Strain H7-Alpha. It is the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S1, S2, S3) | "The outbreak in the village was caused by Strain H7-Alpha. It is a highly mutagenic RNA pathogen. <end_of_turn>" |
| (S1, S3, S2) | "The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha. <end_of_turn>" |
| (S2, S1, S3) | "The epidemic was caused by a highly mutagenic RNA pathogen called Strain H7-Alpha. <end_of_turn>" |
| (S2, S3, S1) | "The epidemic was traced to a highly mutagenic RNA pathogen called Strain H7-Alpha. <end_of_turn>" |
| (S3, S1, S2) | "The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha. <end_of_turn>" |
| (S3, S2, S1) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. This pathogen was identified as Strain H7-Alpha. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 0.9340 | 41.5903 | -8.6402 | 0.0276 | 1.2274 | -0.2550 |
| BERT Similarity | 0.2484 | 0.2885 | 0.1757 | 0.3485 | 0.4049 | 0.2466 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Strain H7-Alpha caused severe respiratory symptoms in laboratory primates."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1448 |
| \{S1\} | -1.7734 | 0.6128 | 0.7576 |
| \{S2\} | 33.9219 | 0.7502 | 0.8950 |
| \{S3\} | 30.1172 | 0.5727 | 0.7175 |
| \{S1, S2\} | 36.4609 | 0.7015 | 0.8463 |
| \{S1, S3\} | 32.5391 | 0.7298 | 0.8746 |
| \{S2, S3\} | 36.9609 | 0.7415 | 0.8863 |
| \{S1, S2, S3\} | 36.2552 | 0.7441 | 0.8889 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The epidemic was caused by a highly mutagenic RNA pathogen. <end_of_turn>" |
| (S2) | "Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients. Therefore, it caused the outbreak in the village. <end_of_turn>" |
| (S3) | "The provided context does not mention a virus outbreak in a village. <end_of_turn>" |
| (S1, S2) | "The outbreak in the village was caused by Strain H7-Alpha. This virus was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S2, S1) | "The epidemic was caused by a highly mutagenic RNA pathogen. Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S1, S3) | "The epidemic was caused by a highly mutagenic RNA pathogen known as Strain H7-Alpha. <end_of_turn>" |
| (S3, S1) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. Strain H7-Alpha was identified as the cause of severe respiratory symptoms in laboratory primates. <end_of_turn>" |
| (S2, S3) | "Strain H7-Alpha, a highly mutagenic RNA pathogen, caused the outbreak in the village. <end_of_turn>" |
| (S3, S2) | "Strain H7-Alpha caused the outbreak in the village. It was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S1, S2, S3) | "The outbreak in the village was caused by Strain H7-Alpha. Strain H7-Alpha is a highly mutagenic RNA pathogen that caused severe respiratory symptoms in laboratory primates. <end_of_turn>" |
| (S1, S3, S2) | "The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha. <end_of_turn>" |
| (S2, S1, S3) | "The epidemic was caused by a highly mutagenic RNA pathogen. Strain H7-Alpha was isolated from the patients and caused severe respiratory symptoms. <end_of_turn>" |
| (S2, S3, S1) | "The epidemic was traced to a highly mutagenic RNA pathogen called Strain H7-Alpha. Strain H7-Alpha caused severe respiratory symptoms in laboratory primates. <end_of_turn>" |
| (S3, S1, S2) | "The outbreak in the village was caused by the highly mutagenic RNA pathogen Strain H7-Alpha. <end_of_turn>" |
| (S3, S2, S1) | "The epidemic was traced to a highly mutagenic RNA pathogen called Strain H7-Alpha. Strain H7-Alpha caused severe respiratory symptoms in laboratory primates. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 0.0004 | 20.0590 | 16.1957 | 0.0000 | 0.5533 | 0.4467 |
| BERT Similarity | 0.2232 | 0.2978 | 0.2232 | 0.2999 | 0.4002 | 0.2999 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A rapidly evolving ribonucleic acid microorganism sparked the community-wide contagion."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1320 |
| \{S1\} | -1.7734 | 0.5870 | 0.7190 |
| \{S2\} | 33.9219 | 0.7424 | 0.8744 |
| \{S3\} | -2.1484 | 0.7676 | 0.8996 |
| \{S1, S2\} | 36.4609 | 0.6937 | 0.8257 |
| \{S1, S3\} | -2.6328 | 0.7019 | 0.8339 |
| \{S2, S3\} | 33.0977 | 0.7894 | 0.9214 |
| \{S1, S2, S3\} | 33.2747 | 0.7898 | 0.9218 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The epidemic was caused by a highly mutagenic RNA pathogen. <end_of_turn>" |
| (S2) | "Strain H7-Alpha, a highly mutagenic RNA pathogen, was isolated from the patients. Therefore, it caused the outbreak in the village. <end_of_turn>" |
| (S3) | "The outbreak in the village was caused by a rapidly evolving ribonucleic acid microorganism. <end_of_turn>" |
| (S1, S2) | "The outbreak in the village was caused by Strain H7-Alpha. This virus was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S2, S1) | "The epidemic was caused by a highly mutagenic RNA pathogen. Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S1, S3) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. This pathogen was a rapidly evolving ribonucleic acid microorganism. <end_of_turn>" |
| (S3, S1) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. <end_of_turn>" |
| (S2, S3) | "Strain H7-Alpha, a rapidly evolving ribonucleic acid microorganism, caused the outbreak in the village. <end_of_turn>" |
| (S3, S2) | "Strain H7-Alpha, a highly mutagenic RNA pathogen, caused the outbreak in the village. <end_of_turn>" |
| (S1, S2, S3) | "The outbreak in the village was caused by a rapidly evolving ribonucleic acid microorganism. This microorganism was identified as Strain H7-Alpha. <end_of_turn>" |
| (S1, S3, S2) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen called Strain H7-Alpha. <end_of_turn>" |
| (S2, S1, S3) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. This pathogen was identified as Strain H7-Alpha. <end_of_turn>" |
| (S2, S3, S1) | "The outbreak in the village was caused by a rapidly evolving ribonucleic acid microorganism known as Strain H7-Alpha. <end_of_turn>" |
| (S3, S1, S2) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |
| (S3, S2, S1) | "The outbreak in the village was caused by a highly mutagenic RNA pathogen. Strain H7-Alpha was the only highly mutagenic RNA pathogen isolated from the patients. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.1897 | 35.5232 | -2.0588 | -0.0057 | 1.0676 | -0.0619 |
| BERT Similarity | 0.1767 | 0.2982 | 0.3149 | 0.2238 | 0.3775 | 0.3987 |

---

### Example 5: Ecology / Bloom

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `-0.1398`

#### Metadata
- **Question**: *"Which compound caused the algal bloom?"*
- **Target Response**: *"Compound NP-8 caused the algal bloom."*
- **S1 (Logical premise 1)**: *"The excessive phytoplankton growth was triggered by a phosphorus-rich agricultural runoff chemical."*
- **S2 (Logical premise 2)**: *"The only phosphorus-rich agricultural runoff chemical detected in the water sample was Compound NP-8."*
- **S3a (Adversarial Distractor)**: *"Chlorophyll is the pigment that gives plants their green color."*
- **S3b (Syntactic Distractor)**: *"Compound NP-8 caused the eutrophication of the nearby freshwater pond."*
- **S3c (Semantic Distractor)**: *"A phosphate-laden farming effluent substance sparked the massive aquatic plant proliferation."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.6200 >= best(S1,S2)=0.6252 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.3329 <= worst(S1,S2)=0.2341 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3262 >= best(S1,S2)=0.3519 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.2195 <= worst(S1,S2)=-0.2296 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Chlorophyll is the pigment that gives plants their green color."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1860 |
| \{S1\} | -14.6562 | 0.7602 | 0.9463 |
| \{S2\} | 18.4922 | 0.4988 | 0.6849 |
| \{S3\} | -16.2266 | 0.6027 | 0.7888 |
| \{S1, S2\} | 20.8047 | 0.7934 | 0.9794 |
| \{S1, S3\} | -15.1172 | 0.7602 | 0.9463 |
| \{S2, S3\} | 17.5078 | 0.6564 | 0.8424 |
| \{S1, S2, S3\} | 18.9036 | 0.8035 | 0.9895 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "A phosphorus-rich agricultural runoff chemical caused the algal bloom. <end_of_turn>" |
| (S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, was detected in the water sample. <end_of_turn>" |
| (S3) | "The provided context does not mention which compound caused an algal bloom. <end_of_turn>" |
| (S1, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S2, S1) | "Compound NP-8 caused the algal bloom. It was the only phosphorus-rich agricultural runoff chemical detected in the water sample. <end_of_turn>" |
| (S1, S3) | "A phosphorus-rich agricultural runoff chemical caused the algal bloom. <end_of_turn>" |
| (S3, S1) | "A phosphorus-rich agricultural runoff chemical caused the algal bloom. <end_of_turn>" |
| (S2, S3) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S3, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, was detected in the water sample. <end_of_turn>" |
| (S1, S2, S3) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S1, S3, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S2, S1, S3) | "Compound NP-8 caused the algal bloom. It was the only phosphorus-rich agricultural runoff chemical detected in the water sample, and excessive phytoplankton growth was triggered by such a chemical. <end_of_turn>" |
| (S2, S3, S1) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S3, S1, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S3, S2, S1) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -3.8498 | 29.0369 | -6.2834 | -0.2037 | 1.5360 | -0.3324 |
| BERT Similarity | 0.3778 | 0.1951 | 0.2305 | 0.4702 | 0.2429 | 0.2869 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Compound NP-8 caused the eutrophication of the nearby freshwater pond."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1860 |
| \{S1\} | -14.6562 | 0.7602 | 0.9463 |
| \{S2\} | 18.4922 | 0.4988 | 0.6849 |
| \{S3\} | 21.3828 | 0.6488 | 0.8348 |
| \{S1, S2\} | 20.8047 | 0.7934 | 0.9794 |
| \{S1, S3\} | 17.7031 | 0.7996 | 0.9856 |
| \{S2, S3\} | 19.8125 | 0.7465 | 0.9325 |
| \{S1, S2, S3\} | 20.2552 | 0.7907 | 0.9767 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "A phosphorus-rich agricultural runoff chemical caused the algal bloom. <end_of_turn>" |
| (S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, was detected in the water sample. <end_of_turn>" |
| (S3) | "Compound NP-8 caused the eutrophication of the nearby freshwater pond, which led to the algal bloom. <end_of_turn>" |
| (S1, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S2, S1) | "Compound NP-8 caused the algal bloom. It was the only phosphorus-rich agricultural runoff chemical detected in the water sample. <end_of_turn>" |
| (S1, S3) | "The compound NP-8 caused the algal bloom. It is a phosphorus-rich agricultural runoff chemical. <end_of_turn>" |
| (S3, S1) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S2, S3) | "Compound NP-8 caused the algal bloom. It is a phosphorus-rich agricultural runoff chemical that led to eutrophication of the pond. <end_of_turn>" |
| (S3, S2) | "Compound NP-8 caused the algal bloom because it is a phosphorus-rich agricultural runoff chemical. <end_of_turn>" |
| (S1, S2, S3) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S1, S3, S2) | "Compound NP-8 caused the algal bloom. It was the only phosphorus-rich agricultural runoff chemical detected in the water sample. <end_of_turn>" |
| (S2, S1, S3) | "Compound NP-8 caused the algal bloom because it is a phosphorus-rich agricultural runoff chemical. <end_of_turn>" |
| (S2, S3, S1) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S3, S1, S2) | "Compound NP-8 caused the algal bloom because it is a phosphorus-rich agricultural runoff chemical. <end_of_turn>" |
| (S3, S2, S1) | "Compound NP-8 caused the algal bloom because it is a phosphorus-rich agricultural runoff chemical. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -4.9657 | 12.6632 | 12.5577 | -0.2452 | 0.6252 | 0.6200 |
| BERT Similarity | 0.3424 | 0.1851 | 0.2632 | 0.4330 | 0.2341 | 0.3329 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A phosphate-laden farming effluent substance sparked the massive aquatic plant proliferation."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1421 |
| \{S1\} | -14.6562 | 0.7421 | 0.8842 |
| \{S2\} | 18.4922 | 0.6259 | 0.7681 |
| \{S3\} | -13.1484 | 0.7203 | 0.8625 |
| \{S1, S2\} | 20.8047 | 0.8373 | 0.9794 |
| \{S1, S3\} | -14.6250 | 0.7498 | 0.8919 |
| \{S2, S3\} | 19.7031 | 0.8167 | 0.9588 |
| \{S1, S2, S3\} | 20.0990 | 0.8236 | 0.9657 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "A phosphorus-rich agricultural runoff chemical caused the algal bloom. <end_of_turn>" |
| (S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, was detected in the water sample. <end_of_turn>" |
| (S3) | "The phosphate-laden farming effluent substance caused the algal bloom. <end_of_turn>" |
| (S1, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S2, S1) | "Compound NP-8 caused the algal bloom. It was the only phosphorus-rich agricultural runoff chemical detected in the water sample. <end_of_turn>" |
| (S1, S3) | "A phosphorus-rich agricultural runoff chemical, specifically a phosphate-laden farming effluent substance, caused the algal bloom. <end_of_turn>" |
| (S3, S1) | "A phosphate-laden farming effluent substance caused the algal bloom. <end_of_turn>" |
| (S2, S3) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S3, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S1, S2, S3) | "Compound NP-8 caused the algal bloom. It was the only phosphorus-rich agricultural runoff chemical detected in the water sample. <end_of_turn>" |
| (S1, S3, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S2, S1, S3) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S2, S3, S1) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S3, S1, S2) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |
| (S3, S2, S1) | "Compound NP-8, a phosphorus-rich agricultural runoff chemical, caused the algal bloom. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -4.6141 | 29.1241 | -4.4110 | -0.2296 | 1.4490 | -0.2195 |
| BERT Similarity | 0.2898 | 0.2652 | 0.2686 | 0.3519 | 0.3220 | 0.3262 |

---

### Example 6: Technology / Gadget

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.0222`

#### Metadata
- **Question**: *"Which kitchen appliance caused the blackout?"*
- **Target Response**: *"The microwave caused the blackout."*
- **S1 (Logical premise 1)**: *"The electrical failure was triggered by a high-wattage heating appliance."*
- **S2 (Logical premise 2)**: *"The only high-wattage heating appliance plugged in was the microwave."*
- **S3a (Adversarial Distractor)**: *"The television consumes very little electricity when in standby mode."*
- **S3b (Syntactic Distractor)**: *"The microwave destroyed the ceramic bowl."*
- **S3c (Semantic Distractor)**: *"The massive power loss was initiated when someone turned on the high-wattage kitchen heating appliance."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.5230 >= best(S1,S2)=0.4752 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.1853 <= worst(S1,S2)=0.3570 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3028 >= best(S1,S2)=0.3940 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=0.0896 <= worst(S1,S2)=-0.0165 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"The television consumes very little electricity when in standby mode."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1555 |
| \{S1\} | -2.3125 | 0.7736 | 0.9291 |
| \{S2\} | 11.0312 | 0.8445 | 1.0000 |
| \{S3\} | -3.2500 | 0.6474 | 0.8028 |
| \{S1, S2\} | 14.8047 | 0.8164 | 0.9719 |
| \{S1, S3\} | -0.7461 | 0.7609 | 0.9163 |
| \{S2, S3\} | 11.1953 | 0.8054 | 0.9609 |
| \{S1, S2, S3\} | 15.1849 | 0.8385 | 0.9940 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The high-wattage heating appliance that caused the blackout was in the kitchen. <end_of_turn>" |
| (S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3) | "The context does not provide information about a blackout or which appliance caused it. <end_of_turn>" |
| (S1, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S2, S1) | "The microwave caused the blackout. The electrical failure was triggered by the microwave, a high-wattage heating appliance. <end_of_turn>" |
| (S1, S3) | "The high-wattage heating appliance in the kitchen caused the blackout. <end_of_turn>" |
| (S3, S1) | "The blackout was caused by a high-wattage heating appliance. <end_of_turn>" |
| (S2, S3) | "The microwave caused the blackout because it is the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3, S2) | "The microwave caused the blackout because it is the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S1, S2, S3) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S1, S3, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S2, S1, S3) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in when the electrical failure occurred. <end_of_turn>" |
| (S2, S3, S1) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3, S1, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3, S2, S1) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 1.6053 | 14.2478 | -0.6682 | 0.1057 | 0.9383 | -0.0440 |
| BERT Similarity | 0.2831 | 0.3409 | 0.2145 | 0.3377 | 0.4065 | 0.2558 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"The microwave destroyed the ceramic bowl."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1555 |
| \{S1\} | -2.3125 | 0.7736 | 0.9291 |
| \{S2\} | 11.0312 | 0.8445 | 1.0000 |
| \{S3\} | 14.5781 | 0.4916 | 0.6471 |
| \{S1, S2\} | 14.8047 | 0.8164 | 0.9719 |
| \{S1, S3\} | 12.7266 | 0.7250 | 0.8804 |
| \{S2, S3\} | 13.9453 | 0.8184 | 0.9738 |
| \{S1, S2, S3\} | 15.3776 | 0.8158 | 0.9713 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The high-wattage heating appliance that caused the blackout was in the kitchen. <end_of_turn>" |
| (S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3) | "The context does not provide information about a blackout. <end_of_turn>" |
| (S1, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S2, S1) | "The microwave caused the blackout. The electrical failure was triggered by the microwave, a high-wattage heating appliance. <end_of_turn>" |
| (S1, S3) | "The high-wattage heating appliance that caused the blackout was the microwave. <end_of_turn>" |
| (S3, S1) | "The electrical failure was triggered by a high-wattage heating appliance, which was likely the microwave. <end_of_turn>" |
| (S2, S3) | "The microwave caused the blackout because it was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3, S2) | "The microwave caused the blackout because it was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S1, S2, S3) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S1, S3, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S2, S1, S3) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in and its failure triggered the electrical issue. <end_of_turn>" |
| (S2, S3, S1) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in and its electrical failure triggered the outage. <end_of_turn>" |
| (S3, S1, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in when the electrical failure occurred. <end_of_turn>" |
| (S3, S2, S1) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in when the electrical failure occurred. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 0.0269 | 7.3082 | 8.0425 | 0.0017 | 0.4752 | 0.5230 |
| BERT Similarity | 0.2912 | 0.3734 | 0.1512 | 0.3570 | 0.4577 | 0.1853 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"The massive power loss was initiated when someone turned on the high-wattage kitchen heating appliance."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1647 |
| \{S1\} | -2.3125 | 0.7255 | 0.8903 |
| \{S2\} | 11.0312 | 0.7811 | 0.9458 |
| \{S3\} | 0.4375 | 0.7248 | 0.8895 |
| \{S1, S2\} | 14.8047 | 0.7788 | 0.9436 |
| \{S1, S3\} | -0.0273 | 0.6920 | 0.8567 |
| \{S2, S3\} | 15.2734 | 0.7789 | 0.9437 |
| \{S1, S2, S3\} | 15.1823 | 0.7844 | 0.9491 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The high-wattage heating appliance that caused the blackout was in the kitchen. <end_of_turn>" |
| (S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3) | "The high-wattage kitchen heating appliance caused the blackout. <end_of_turn>" |
| (S1, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S2, S1) | "The microwave caused the blackout. The electrical failure was triggered by the microwave, a high-wattage heating appliance. <end_of_turn>" |
| (S1, S3) | "The high-wattage kitchen heating appliance caused the blackout. Someone turned it on, initiating the massive power loss. <end_of_turn>" |
| (S3, S1) | "The high-wattage kitchen heating appliance caused the blackout. <end_of_turn>" |
| (S2, S3) | "The microwave caused the blackout. Someone turned on the microwave, which is a high-wattage heating appliance, initiating the power loss. <end_of_turn>" |
| (S3, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S1, S2, S3) | "The microwave caused the blackout. Someone turned on the microwave, which is a high-wattage heating appliance. <end_of_turn>" |
| (S1, S3, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S2, S1, S3) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in and its activation triggered the electrical failure. <end_of_turn>" |
| (S2, S3, S1) | "The microwave caused the blackout. Someone turned on the microwave, which overloaded the electrical system. <end_of_turn>" |
| (S3, S1, S2) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |
| (S3, S2, S1) | "The microwave caused the blackout. It was the only high-wattage heating appliance plugged in. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.2498 | 14.0725 | 1.3596 | -0.0165 | 0.9269 | 0.0896 |
| BERT Similarity | 0.2378 | 0.3091 | 0.2375 | 0.3032 | 0.3940 | 0.3028 |

---

### Example 7: Weapon / Armor

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.2075`

#### Metadata
- **Question**: *"Which weapon pierced the knight's armor?"*
- **Target Response**: *"The crossbow pierced the knight's armor."*
- **S1 (Logical premise 1)**: *"The metal plating was punctured by a ranged firing mechanism."*
- **S2 (Logical premise 2)**: *"The only ranged firing mechanism on the battlefield was the crossbow."*
- **S3a (Adversarial Distractor)**: *"The dull training sword is completely harmless in real combat."*
- **S3b (Syntactic Distractor)**: *"The crossbow pierced the wooden target."*
- **S3c (Semantic Distractor)**: *"A mechanical bolt-launching weapon pierced the knight's armor during the battle."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.4067 >= best(S1,S2)=0.4964 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.1295 <= worst(S1,S2)=0.3867 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3706 >= best(S1,S2)=0.3303 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=0.1027 <= worst(S1,S2)=0.1024 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"The dull training sword is completely harmless in real combat."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.4129 |
| \{S1\} | 4.4453 | 0.4629 | 0.8758 |
| \{S2\} | 19.5391 | 0.5871 | 1.0000 |
| \{S3\} | -0.1406 | 0.3244 | 0.7373 |
| \{S1, S2\} | 22.6641 | 0.5871 | 1.0000 |
| \{S1, S3\} | 6.1914 | 0.4629 | 0.8758 |
| \{S2, S3\} | 19.2422 | 0.4563 | 0.8692 |
| \{S1, S2, S3\} | 22.1380 | 0.5322 | 0.9451 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "A ranged firing mechanism pierced the knight's armor. <end_of_turn>" |
| (S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S3) | "The context does not provide information about a knight or a weapon piercing their armor. <end_of_turn>" |
| (S1, S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S2, S1) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S1, S3) | "A ranged firing mechanism pierced the knight's armor. <end_of_turn>" |
| (S3, S1) | "A ranged firing mechanism pierced the knight's armor. <end_of_turn>" |
| (S2, S3) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S3, S2) | "The context does not state which weapon pierced the knight's armor. It only mentions a training sword and a crossbow. <end_of_turn>" |
| (S1, S2, S3) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S1, S3, S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S2, S1, S3) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S2, S3, S1) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S3, S1, S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S3, S2, S1) | "The metal plating was punctured by a ranged firing mechanism, which was the crossbow. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 4.0232 | 18.0955 | 0.0193 | 0.1817 | 0.8174 | 0.0009 |
| BERT Similarity | 0.2027 | 0.2615 | 0.0680 | 0.3809 | 0.4913 | 0.1278 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"The crossbow pierced the wooden target."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.4129 |
| \{S1\} | 4.4453 | 0.4629 | 0.8758 |
| \{S2\} | 19.5391 | 0.5871 | 1.0000 |
| \{S3\} | 18.6016 | 0.3508 | 0.7637 |
| \{S1, S2\} | 22.6641 | 0.5871 | 1.0000 |
| \{S1, S3\} | 19.6562 | 0.4351 | 0.8481 |
| \{S2, S3\} | 22.1406 | 0.4174 | 0.8303 |
| \{S1, S2, S3\} | 21.9922 | 0.5478 | 0.9607 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "A ranged firing mechanism pierced the knight's armor. <end_of_turn>" |
| (S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S3) | "The context does not say which weapon pierced the knight's armor. It only says that a crossbow pierced a wooden target. <end_of_turn>" |
| (S1, S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S2, S1) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S1, S3) | "A ranged firing mechanism, specifically a crossbow, pierced the knight's armor. <end_of_turn>" |
| (S3, S1) | "A ranged firing mechanism, likely a crossbow, pierced the knight's armor. <end_of_turn>" |
| (S2, S3) | "The crossbow pierced the wooden target, so it is likely the weapon that pierced the knight's armor. <end_of_turn>" |
| (S3, S2) | "The crossbow pierced the knight's armor because it was the only ranged firing mechanism on the battlefield. <end_of_turn>" |
| (S1, S2, S3) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S1, S3, S2) | "The crossbow pierced the knight's armor. It was the only ranged firing mechanism on the battlefield. <end_of_turn>" |
| (S2, S1, S3) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S2, S3, S1) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S3, S1, S2) | "The crossbow pierced the knight's armor. It was the only ranged firing mechanism on the battlefield. <end_of_turn>" |
| (S3, S2, S1) | "The crossbow pierced the knight's armor. It was the only ranged firing mechanism on the battlefield. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 2.1289 | 10.9180 | 8.9453 | 0.0968 | 0.4964 | 0.4067 |
| BERT Similarity | 0.2118 | 0.2650 | 0.0709 | 0.3867 | 0.4838 | 0.1295 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A mechanical bolt-launching weapon pierced the knight's armor during the battle."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.3446 |
| \{S1\} | 4.4453 | 0.5669 | 0.9115 |
| \{S2\} | 19.5391 | 0.5893 | 0.9339 |
| \{S3\} | 5.0703 | 0.6179 | 0.9625 |
| \{S1, S2\} | 22.6641 | 0.5893 | 0.9339 |
| \{S1, S3\} | 5.8320 | 0.6111 | 0.9557 |
| \{S2, S3\} | 22.0547 | 0.6277 | 0.9723 |
| \{S1, S2, S3\} | 22.6094 | 0.6253 | 0.9699 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "A ranged firing mechanism pierced the knight's armor. <end_of_turn>" |
| (S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S3) | "A mechanical bolt-launching weapon pierced the knight's armor. <end_of_turn>" |
| (S1, S2) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S2, S1) | "The crossbow pierced the knight's armor. <end_of_turn>" |
| (S1, S3) | "A mechanical bolt-launching weapon pierced the knight's armor during the battle. <end_of_turn>" |
| (S3, S1) | "A mechanical bolt-launching weapon pierced the knight's armor. <end_of_turn>" |
| (S2, S3) | "A mechanical bolt-launching weapon, likely a crossbow, pierced the knight's armor. <end_of_turn>" |
| (S3, S2) | "A mechanical bolt-launching weapon, which was a crossbow, pierced the knight's armor. <end_of_turn>" |
| (S1, S2, S3) | "A mechanical bolt-launching weapon, the crossbow, pierced the knight's armor. <end_of_turn>" |
| (S1, S3, S2) | "A mechanical bolt-launching weapon, specifically a crossbow, pierced the knight's armor. <end_of_turn>" |
| (S2, S1, S3) | "A mechanical bolt-launching weapon, likely a crossbow, pierced the knight's armor. <end_of_turn>" |
| (S2, S3, S1) | "A mechanical bolt-launching weapon, the crossbow, pierced the knight's armor. <end_of_turn>" |
| (S3, S1, S2) | "A crossbow pierced the knight's armor during the battle. <end_of_turn>" |
| (S3, S2, S1) | "The crossbow pierced the knight's armor during the battle. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 2.3145 | 17.9727 | 2.3223 | 0.1024 | 0.7949 | 0.1027 |
| BERT Similarity | 0.1871 | 0.2065 | 0.2317 | 0.2991 | 0.3303 | 0.3706 |

---

### Example 8: Acoustics / Feedback

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.0142`

#### Metadata
- **Question**: *"Which device caused the audio feedback?"*
- **Target Response**: *"Module AC-4 caused the audio feedback."*
- **S1 (Logical premise 1)**: *"The high-pitched acoustic resonance was triggered by a gain-loop amplifier signal."*
- **S2 (Logical premise 2)**: *"The only gain-loop amplifier signal detected in the sound system was Module AC-4."*
- **S3a (Adversarial Distractor)**: *"Dynamic microphones are commonly used in live performances due to their durability."*
- **S3b (Syntactic Distractor)**: *"Module AC-4 caused the speaker cone to vibrate during calibration."*
- **S3c (Semantic Distractor)**: *"A volume-amplified sound frequency loop generated the screeching noise distortion."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.5146 >= best(S1,S2)=0.5295 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.2545 <= worst(S1,S2)=0.3609 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.2941 >= best(S1,S2)=0.3879 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.0599 <= worst(S1,S2)=-0.0433 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Dynamic microphones are commonly used in live performances due to their durability."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1021 |
| \{S1\} | -3.6484 | 0.7256 | 0.8277 |
| \{S2\} | 32.2500 | 0.7814 | 0.8835 |
| \{S3\} | -9.1719 | 0.5614 | 0.6635 |
| \{S1, S2\} | 32.7266 | 0.8146 | 0.9167 |
| \{S1, S3\} | -5.2539 | 0.6625 | 0.7646 |
| \{S2, S3\} | 30.6797 | 0.7150 | 0.8171 |
| \{S1, S2, S3\} | 30.2135 | 0.8044 | 0.9065 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The gain-loop amplifier signal caused the audio feedback. <end_of_turn>" |
| (S2) | "Module AC-4 caused the audio feedback. <end_of_turn>" |
| (S3) | "The context does not provide information about any device causing audio feedback. <end_of_turn>" |
| (S1, S2) | "Module AC-4 caused the audio feedback. It was the only gain-loop amplifier signal detected in the sound system. <end_of_turn>" |
| (S2, S1) | "Module AC-4 caused the audio feedback. The high-pitched acoustic resonance was triggered by its gain-loop amplifier signal. <end_of_turn>" |
| (S1, S3) | "The gain-loop amplifier signal caused the audio feedback. <end_of_turn>" |
| (S3, S1) | "The context does not specify which device caused the audio feedback. <end_of_turn>" |
| (S2, S3) | "The audio feedback was caused by Module AC-4. <end_of_turn>" |
| (S3, S2) | "The context does not provide information about which device caused the audio feedback. <end_of_turn>" |
| (S1, S2, S3) | "The gain-loop amplifier signal detected in the sound system, Module AC-4, caused the audio feedback. <end_of_turn>" |
| (S1, S3, S2) | "The gain-loop amplifier signal detected in the sound system was from Module AC-4. This device caused the audio feedback. <end_of_turn>" |
| (S2, S1, S3) | "Module AC-4 caused the audio feedback. The high-pitched acoustic resonance was triggered by its gain-loop amplifier signal. <end_of_turn>" |
| (S2, S3, S1) | "Module AC-4 caused the audio feedback. <end_of_turn>" |
| (S3, S1, S2) | "The gain-loop amplifier signal detected in the sound system, Module AC-4, caused the high-pitched acoustic resonance and audio feedback. <end_of_turn>" |
| (S3, S2, S1) | "The high-pitched acoustic resonance, or audio feedback, was triggered by the gain-loop amplifier signal detected in Module AC-4. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.6391 | 35.2769 | -4.4243 | -0.0212 | 1.1676 | -0.1464 |
| BERT Similarity | 0.2940 | 0.3482 | 0.1621 | 0.3656 | 0.4329 | 0.2016 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Module AC-4 caused the speaker cone to vibrate during calibration."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1224 |
| \{S1\} | -3.6484 | 0.7365 | 0.8588 |
| \{S2\} | 32.2500 | 0.7979 | 0.9202 |
| \{S3\} | 32.7188 | 0.6785 | 0.8009 |
| \{S1, S2\} | 32.7266 | 0.8005 | 0.9229 |
| \{S1, S3\} | 31.2891 | 0.7301 | 0.8525 |
| \{S2, S3\} | 32.6328 | 0.7033 | 0.8257 |
| \{S1, S2, S3\} | 32.4583 | 0.7294 | 0.8517 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The gain-loop amplifier signal caused the audio feedback. <end_of_turn>" |
| (S2) | "Module AC-4 caused the audio feedback. <end_of_turn>" |
| (S3) | "Module AC-4 caused the audio feedback. Its vibration during calibration led to the speaker cone vibrating. <end_of_turn>" |
| (S1, S2) | "Module AC-4 caused the audio feedback. It was the only gain-loop amplifier signal detected in the sound system. <end_of_turn>" |
| (S2, S1) | "Module AC-4 caused the audio feedback. The high-pitched acoustic resonance was triggered by its gain-loop amplifier signal. <end_of_turn>" |
| (S1, S3) | "Module AC-4 caused the audio feedback. Its gain-loop amplifier signal triggered the high-pitched acoustic resonance. <end_of_turn>" |
| (S3, S1) | "Module AC-4 caused the audio feedback. Its gain-loop amplifier signal triggered a high-pitched acoustic resonance that vibrated the speaker cone. <end_of_turn>" |
| (S2, S3) | "Module AC-4 caused the audio feedback. It created a gain-loop amplifier signal that made the speaker cone vibrate during calibration. <end_of_turn>" |
| (S3, S2) | "Module AC-4 caused the audio feedback because its gain-loop amplifier signal caused the speaker cone to vibrate. <end_of_turn>" |
| (S1, S2, S3) | "Module AC-4, a gain-loop amplifier signal, caused the audio feedback. <end_of_turn>" |
| (S1, S3, S2) | "Module AC-4 caused the audio feedback. Its gain-loop amplifier signal triggered the speaker cone to vibrate during calibration. <end_of_turn>" |
| (S2, S1, S3) | "Module AC-4 caused the audio feedback. Its gain-loop amplifier signal triggered a high-pitched acoustic resonance that caused the speaker cone to vibrate. <end_of_turn>" |
| (S2, S3, S1) | "Module AC-4 caused the audio feedback. Its gain-loop amplifier signal triggered a high-pitched acoustic resonance that vibrated the speaker cone. <end_of_turn>" |
| (S3, S1, S2) | "Module AC-4 caused the audio feedback. Its gain-loop amplifier signal triggered a high-pitched acoustic resonance that vibrated the speaker cone. <end_of_turn>" |
| (S3, S2, S1) | "Module AC-4 caused the audio feedback. Its gain-loop amplifier signal triggered a high-pitched acoustic resonance. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.4332 | 17.1879 | 16.7036 | -0.0442 | 0.5295 | 0.5146 |
| BERT Similarity | 0.2632 | 0.2805 | 0.1856 | 0.3609 | 0.3846 | 0.2545 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A volume-amplified sound frequency loop generated the screeching noise distortion."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1191 |
| \{S1\} | -3.6484 | 0.7303 | 0.8494 |
| \{S2\} | 32.2500 | 0.7971 | 0.9162 |
| \{S3\} | -3.9297 | 0.7150 | 0.8341 |
| \{S1, S2\} | 32.7266 | 0.7975 | 0.9165 |
| \{S1, S3\} | -4.2070 | 0.7303 | 0.8494 |
| \{S2, S3\} | 31.9609 | 0.7748 | 0.8939 |
| \{S1, S2, S3\} | 31.4297 | 0.7949 | 0.9140 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The gain-loop amplifier signal caused the audio feedback. <end_of_turn>" |
| (S2) | "Module AC-4 caused the audio feedback. <end_of_turn>" |
| (S3) | "The volume-amplified sound frequency loop caused the audio feedback. <end_of_turn>" |
| (S1, S2) | "Module AC-4 caused the audio feedback. It was the only gain-loop amplifier signal detected in the sound system. <end_of_turn>" |
| (S2, S1) | "Module AC-4 caused the audio feedback. The high-pitched acoustic resonance was triggered by its gain-loop amplifier signal. <end_of_turn>" |
| (S1, S3) | "The gain-loop amplifier signal caused the audio feedback. <end_of_turn>" |
| (S3, S1) | "The gain-loop amplifier signal caused the audio feedback. <end_of_turn>" |
| (S2, S3) | "Module AC-4 caused the audio feedback. It generated a volume-amplified sound frequency loop that created the screeching noise distortion. <end_of_turn>" |
| (S3, S2) | "Module AC-4, a gain-loop amplifier signal, caused the audio feedback. <end_of_turn>" |
| (S1, S2, S3) | "Module AC-4, a gain-loop amplifier, caused the audio feedback. <end_of_turn>" |
| (S1, S3, S2) | "The gain-loop amplifier signal detected in the sound system was from Module AC-4. This device caused the audio feedback. <end_of_turn>" |
| (S2, S1, S3) | "Module AC-4 caused the audio feedback. It generated a volume-amplified sound frequency loop that created the screeching noise distortion. <end_of_turn>" |
| (S2, S3, S1) | "Module AC-4 caused the audio feedback. It generated a volume-amplified sound frequency loop that created the screeching noise distortion. <end_of_turn>" |
| (S3, S1, S2) | "Module AC-4, the gain-loop amplifier signal, caused the audio feedback. <end_of_turn>" |
| (S3, S2, S1) | "Module AC-4, a gain-loop amplifier signal, caused the audio feedback. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.3600 | 34.6732 | -1.8835 | -0.0433 | 1.1032 | -0.0599 |
| BERT Similarity | 0.2528 | 0.3084 | 0.2338 | 0.3180 | 0.3879 | 0.2941 |

---

### Example 9: History / Document

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `-0.1934`

#### Metadata
- **Question**: *"Which document established the peace treaty?"*
- **Target Response**: *"The Treaty of Utrecht established the peace treaty."*
- **S1 (Logical premise 1)**: *"The peace agreement was settled by the pact signed in the year 1713."*
- **S2 (Logical premise 2)**: *"The only pact signed in the year 1713 to end the war was the Treaty of Utrecht."*
- **S3a (Adversarial Distractor)**: *"The Magna Carta was signed in 1215 to limit the power of the king."*
- **S3b (Syntactic Distractor)**: *"The Treaty of Utrecht redrew the map of Europe."*
- **S3c (Semantic Distractor)**: *"The international pact signed in 1713 resolved the war."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.5680 >= best(S1,S2)=0.5857 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.3469 <= worst(S1,S2)=0.3178 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.2953 >= best(S1,S2)=0.3899 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.0963 <= worst(S1,S2)=-0.1483 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"The Magna Carta was signed in 1215 to limit the power of the king."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1964 |
| \{S1\} | -3.4609 | 0.6866 | 0.8829 |
| \{S2\} | 11.3828 | 0.7128 | 0.9092 |
| \{S3\} | -15.4297 | 0.4231 | 0.6195 |
| \{S1, S2\} | 11.1172 | 0.7202 | 0.9166 |
| \{S1, S3\} | -4.2930 | 0.6781 | 0.8744 |
| \{S2, S3\} | 11.2891 | 0.7736 | 0.9699 |
| \{S1, S2, S3\} | 9.9818 | 0.7621 | 0.9585 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The peace treaty was established by the pact signed in the year 1713. <end_of_turn>" |
| (S2) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S3) | "The provided context does not mention a peace treaty. <end_of_turn>" |
| (S1, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S2, S1) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S1, S3) | "The peace treaty was established by the pact signed in the year 1713. <end_of_turn>" |
| (S3, S1) | "The peace agreement was established by the pact signed in the year 1713. <end_of_turn>" |
| (S2, S3) | "The Treaty of Utrecht established the peace treaty. It was signed in 1713 to end the war. <end_of_turn>" |
| (S3, S2) | "The Treaty of Utrecht established the peace treaty. It was signed in 1713 to end the war. <end_of_turn>" |
| (S1, S2, S3) | "The peace treaty was established by the Treaty of Utrecht. It was signed in 1713 to end the war. <end_of_turn>" |
| (S1, S3, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S2, S1, S3) | "The Treaty of Utrecht established the peace treaty. The peace agreement was settled by the pact signed in 1713. <end_of_turn>" |
| (S2, S3, S1) | "The peace treaty was established by the Treaty of Utrecht, signed in 1713. <end_of_turn>" |
| (S3, S1, S2) | "The peace treaty was established by the Treaty of Utrecht. It was signed in 1713 to end the war. <end_of_turn>" |
| (S3, S2, S1) | "The peace agreement was settled by the Treaty of Utrecht, signed in 1713. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 0.2224 | 15.4353 | -5.6760 | 0.0223 | 1.5464 | -0.5686 |
| BERT Similarity | 0.2688 | 0.3296 | 0.1637 | 0.3527 | 0.4325 | 0.2148 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"The Treaty of Utrecht redrew the map of Europe."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2040 |
| \{S1\} | -3.4609 | 0.6671 | 0.8711 |
| \{S2\} | 11.3828 | 0.7002 | 0.9042 |
| \{S3\} | 11.5859 | 0.7002 | 0.9042 |
| \{S1, S2\} | 11.1172 | 0.7102 | 0.9141 |
| \{S1, S3\} | 10.5391 | 0.7273 | 0.9312 |
| \{S2, S3\} | 11.4375 | 0.7202 | 0.9241 |
| \{S1, S2, S3\} | 10.6458 | 0.7392 | 0.9432 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The peace treaty was established by the pact signed in the year 1713. <end_of_turn>" |
| (S2) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S3) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S1, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S2, S1) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S1, S3) | "The peace treaty was established by the pact signed in 1713. The Treaty of Utrecht is the name of the document that established the peace. <end_of_turn>" |
| (S3, S1) | "The peace treaty was established by the pact signed in 1713. This pact is known as the Treaty of Utrecht. <end_of_turn>" |
| (S2, S3) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S3, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S1, S2, S3) | "The peace treaty was established by the Treaty of Utrecht. The Treaty of Utrecht was signed in 1713 to end the war. <end_of_turn>" |
| (S1, S3, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S2, S1, S3) | "The Treaty of Utrecht established the peace treaty. The peace agreement was settled by the pact signed in 1713. <end_of_turn>" |
| (S2, S3, S1) | "The peace treaty was established by the Treaty of Utrecht, signed in 1713. <end_of_turn>" |
| (S3, S1, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S3, S2, S1) | "The Treaty of Utrecht established the peace treaty. The peace agreement was settled by the pact signed in the year 1713. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.6363 | 6.2348 | 6.0473 | -0.1537 | 0.5857 | 0.5680 |
| BERT Similarity | 0.2349 | 0.2479 | 0.2564 | 0.3178 | 0.3353 | 0.3469 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"The international pact signed in 1713 resolved the war."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.2331 |
| \{S1\} | -3.4609 | 0.6192 | 0.8523 |
| \{S2\} | 11.3828 | 0.7013 | 0.9344 |
| \{S3\} | -2.5078 | 0.6144 | 0.8475 |
| \{S1, S2\} | 11.1172 | 0.6747 | 0.9078 |
| \{S1, S3\} | -3.5820 | 0.6252 | 0.8583 |
| \{S2, S3\} | 11.2734 | 0.6513 | 0.8844 |
| \{S1, S2, S3\} | 10.6615 | 0.7210 | 0.9541 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The peace treaty was established by the pact signed in the year 1713. <end_of_turn>" |
| (S2) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S3) | "The international pact signed in 1713 established the peace treaty. <end_of_turn>" |
| (S1, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S2, S1) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S1, S3) | "The peace treaty was established by the international pact signed in 1713. <end_of_turn>" |
| (S3, S1) | "The international pact signed in 1713 established the peace treaty. The peace agreement was settled by this pact. <end_of_turn>" |
| (S2, S3) | "The Treaty of Utrecht established the peace treaty. The international pact signed in 1713 resolved the war. <end_of_turn>" |
| (S3, S2) | "The Treaty of Utrecht established the peace treaty. It was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S1, S2, S3) | "The peace treaty was established by the Treaty of Utrecht. <end_of_turn>" |
| (S1, S3, S2) | "The peace treaty was established by the Treaty of Utrecht. The Treaty of Utrecht was the only pact signed in 1713 to end the war. <end_of_turn>" |
| (S2, S1, S3) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S2, S3, S1) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S3, S1, S2) | "The Treaty of Utrecht established the peace treaty. <end_of_turn>" |
| (S3, S2, S1) | "The peace treaty was established by the Treaty of Utrecht. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.5809 | 13.2687 | -1.0263 | -0.1483 | 1.2445 | -0.0963 |
| BERT Similarity | 0.2270 | 0.2811 | 0.2129 | 0.3149 | 0.3899 | 0.2953 |

---

### Example 10: Sports / Athlete

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.1173`

#### Metadata
- **Question**: *"Which athlete won the marathon?"*
- **Target Response**: *"Runner 104 won the marathon."*
- **S1 (Logical premise 1)**: *"The gold medal was claimed by the competitor representing the Swedish delegation."*
- **S2 (Logical premise 2)**: *"The only competitor representing the Swedish delegation in the race was Runner 104."*
- **S3a (Adversarial Distractor)**: *"Runner 205 fell down near the water station during the race."*
- **S3b (Syntactic Distractor)**: *"Runner 104 won the marathon event at the youth championship."*
- **S3c (Semantic Distractor)**: *"The competitor representing the Swedish delegation won the marathon."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.6029 >= best(S1,S2)=0.5431 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.3020 <= worst(S1,S2)=0.3369 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3224 >= best(S1,S2)=0.3406 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.2246 <= worst(S1,S2)=-0.1839 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Runner 205 fell down near the water station during the race."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1157 |
| \{S1\} | -10.9609 | 0.7937 | 0.9094 |
| \{S2\} | 17.2422 | 0.7228 | 0.8384 |
| \{S3\} | -0.0156 | 0.5684 | 0.6841 |
| \{S1, S2\} | 20.6641 | 0.8843 | 1.0000 |
| \{S1, S3\} | 0.5898 | 0.7918 | 0.9075 |
| \{S2, S3\} | 13.5625 | 0.5668 | 0.6825 |
| \{S1, S2, S3\} | 19.6641 | 0.8843 | 1.0000 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The athlete representing the Swedish delegation won the marathon. <end_of_turn>" |
| (S2) | "The context does not say who won the marathon. It only states that Runner 104 represented Sweden. <end_of_turn>" |
| (S3) | "The provided context does not say who won the marathon. <end_of_turn>" |
| (S1, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S1) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S1, S3) | "The athlete representing the Swedish delegation won the marathon. <end_of_turn>" |
| (S3, S1) | "The competitor representing the Swedish delegation won the marathon. <end_of_turn>" |
| (S2, S3) | "The provided context does not state which athlete won the marathon. <end_of_turn>" |
| (S3, S2) | "The provided context does not state which athlete won the marathon. <end_of_turn>" |
| (S1, S2, S3) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S1, S3, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S1, S3) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S3, S1) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S3, S1, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S3, S2, S1) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.9486 | 19.6393 | 0.9733 | -0.0482 | 0.9987 | 0.0495 |
| BERT Similarity | 0.4346 | 0.2866 | 0.1631 | 0.4914 | 0.3241 | 0.1845 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Runner 104 won the marathon event at the youth championship."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1026 |
| \{S1\} | -10.9609 | 0.8088 | 0.9114 |
| \{S2\} | 17.2422 | 0.7345 | 0.8371 |
| \{S3\} | 19.8984 | 0.7621 | 0.8647 |
| \{S1, S2\} | 20.6641 | 0.8907 | 0.9933 |
| \{S1, S3\} | 20.5781 | 0.8027 | 0.9053 |
| \{S2, S3\} | 21.9766 | 0.8352 | 0.9378 |
| \{S1, S2, S3\} | 21.4818 | 0.8637 | 0.9663 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The athlete representing the Swedish delegation won the marathon. <end_of_turn>" |
| (S2) | "The context does not say who won the marathon. It only states that Runner 104 represented Sweden. <end_of_turn>" |
| (S3) | "Runner 104 won the marathon event. <end_of_turn>" |
| (S1, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S1) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S1, S3) | "Runner 104 won the marathon event. <end_of_turn>" |
| (S3, S1) | "Runner 104 won the marathon event. They represented the Swedish delegation. <end_of_turn>" |
| (S2, S3) | "Runner 104 won the marathon event. They were the only competitor representing the Swedish delegation in the race. <end_of_turn>" |
| (S3, S2) | "Runner 104 won the marathon. They were the only competitor representing the Swedish delegation in the race. <end_of_turn>" |
| (S1, S2, S3) | "Runner 104, representing the Swedish delegation, won the marathon event. <end_of_turn>" |
| (S1, S3, S2) | "Runner 104 won the marathon. They were the only competitor representing the Swedish delegation in the race. <end_of_turn>" |
| (S2, S1, S3) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S3, S1) | "Runner 104, representing the Swedish delegation, won the marathon event. <end_of_turn>" |
| (S3, S1, S2) | "Runner 104 won the marathon. They were the only competitor representing the Swedish delegation in the race. <end_of_turn>" |
| (S3, S2, S1) | "Runner 104 won the marathon. They were the only competitor representing the Swedish delegation in the race. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -3.1350 | 11.6658 | 12.9510 | -0.1459 | 0.5431 | 0.6029 |
| BERT Similarity | 0.3119 | 0.2910 | 0.2608 | 0.3611 | 0.3369 | 0.3020 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"The competitor representing the Swedish delegation won the marathon."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1157 |
| \{S1\} | -10.9609 | 0.7937 | 0.9094 |
| \{S2\} | 17.2422 | 0.7228 | 0.8384 |
| \{S3\} | -14.2188 | 0.7937 | 0.9094 |
| \{S1, S2\} | 20.6641 | 0.8843 | 1.0000 |
| \{S1, S3\} | -14.2539 | 0.7875 | 0.9032 |
| \{S2, S3\} | 22.2656 | 0.8522 | 0.9679 |
| \{S1, S2, S3\} | 20.3229 | 0.8843 | 1.0000 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The athlete representing the Swedish delegation won the marathon. <end_of_turn>" |
| (S2) | "The context does not say who won the marathon. It only states that Runner 104 represented Sweden. <end_of_turn>" |
| (S3) | "The athlete representing the Swedish delegation won the marathon. <end_of_turn>" |
| (S1, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S1) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S1, S3) | "The athlete representing the Swedish delegation won the marathon. <end_of_turn>" |
| (S3, S1) | "The athlete representing the Swedish delegation won the marathon. They also claimed the gold medal. <end_of_turn>" |
| (S2, S3) | "Runner 104 won the marathon. They were the only competitor representing the Swedish delegation in the race. <end_of_turn>" |
| (S3, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S1, S2, S3) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S1, S3, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S1, S3) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S2, S3, S1) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S3, S1, S2) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |
| (S3, S2, S1) | "Runner 104, representing the Swedish delegation, won the marathon. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -3.7368 | 28.6246 | -4.5649 | -0.1839 | 1.4085 | -0.2246 |
| BERT Similarity | 0.3012 | 0.2980 | 0.2851 | 0.3406 | 0.3370 | 0.3224 |

---

### Example 11: Aviation / Incident

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `-0.1452`

#### Metadata
- **Question**: *"Which aircraft caused the runway collision?"*
- **Target Response**: *"Flight Alpha-9 caused the runway collision."*
- **S1 (Logical premise 1)**: *"The airport accident was triggered by a twin-engine commercial jetliner."*
- **S2 (Logical premise 2)**: *"The only twin-engine commercial jetliner taxiing at that time was Flight Alpha-9."*
- **S3a (Adversarial Distractor)**: *"Helicopters require a landing pad and can hover in place."*
- **S3b (Syntactic Distractor)**: *"Flight Alpha-9 caused a minor runway collision during a simulator test."*
- **S3c (Semantic Distractor)**: *"A twin-engine commercial jetliner caused the runway collision."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.5903 >= best(S1,S2)=0.5056 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.4101 <= worst(S1,S2)=0.2631 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3312 >= best(S1,S2)=0.3633 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.0374 <= worst(S1,S2)=-0.0882 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Helicopters require a landing pad and can hover in place."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1825 |
| \{S1\} | -6.6016 | 0.7800 | 0.9625 |
| \{S2\} | 25.9141 | 0.7377 | 0.9202 |
| \{S3\} | -11.7188 | 0.5330 | 0.7155 |
| \{S1, S2\} | 25.8750 | 0.7774 | 0.9599 |
| \{S1, S3\} | -6.1719 | 0.6084 | 0.7909 |
| \{S2, S3\} | 24.1406 | 0.6796 | 0.8621 |
| \{S1, S2, S3\} | 22.9492 | 0.7623 | 0.9448 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The twin-engine commercial jetliner caused the runway collision. <end_of_turn>" |
| (S2) | "Flight Alpha-9, the only twin-engine commercial jetliner taxiing, caused the runway collision. <end_of_turn>" |
| (S3) | "The context does not provide information about a runway collision or the type of aircraft involved. <end_of_turn>" |
| (S1, S2) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision. <end_of_turn>" |
| (S2, S1) | "The twin-engine commercial jetliner taxiing at the time, Flight Alpha-9, caused the runway collision. <end_of_turn>" |
| (S1, S3) | "The twin-engine commercial jetliner caused the runway collision. Helicopters require a landing pad and can hover in place. <end_of_turn>" |
| (S3, S1) | "The runway collision was caused by a twin-engine commercial jetliner. <end_of_turn>" |
| (S2, S3) | "The runway collision was caused by Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time. <end_of_turn>" |
| (S3, S2) | "The context states that Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time. Therefore, Flight Alpha-9 caused the runway collision. <end_of_turn>" |
| (S1, S2, S3) | "The twin-engine commercial jetliner, Flight Alpha-9, caused the runway collision. <end_of_turn>" |
| (S1, S3, S2) | "The twin-engine commercial jetliner, Flight Alpha-9, caused the runway collision. <end_of_turn>" |
| (S2, S1, S3) | "The twin-engine commercial jetliner, Flight Alpha-9, caused the runway collision. <end_of_turn>" |
| (S2, S3, S1) | "The runway collision was caused by Flight Alpha-9, a twin-engine commercial jetliner. <end_of_turn>" |
| (S3, S1, S2) | "The runway collision was caused by Flight Alpha-9, a twin-engine commercial jetliner. <end_of_turn>" |
| (S3, S2, S1) | "The airport accident was triggered by Flight Alpha-9, a twin-engine commercial jetliner. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.6797 | 29.7344 | -5.1055 | -0.0732 | 1.2957 | -0.2225 |
| BERT Similarity | 0.3068 | 0.3212 | 0.1344 | 0.4024 | 0.4213 | 0.1763 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Flight Alpha-9 caused a minor runway collision during a simulator test."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1196 |
| \{S1\} | -6.6016 | 0.6493 | 0.7689 |
| \{S2\} | 25.9141 | 0.7541 | 0.8737 |
| \{S3\} | 30.1328 | 0.7714 | 0.8910 |
| \{S1, S2\} | 25.8750 | 0.7060 | 0.8256 |
| \{S1, S3\} | 26.2500 | 0.8259 | 0.9455 |
| \{S2, S3\} | 26.3359 | 0.8259 | 0.9455 |
| \{S1, S2, S3\} | 27.1042 | 0.8235 | 0.9431 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The twin-engine commercial jetliner caused the runway collision. <end_of_turn>" |
| (S2) | "Flight Alpha-9, the only twin-engine commercial jetliner taxiing, caused the runway collision. <end_of_turn>" |
| (S3) | "Flight Alpha-9 caused the runway collision during a simulator test. <end_of_turn>" |
| (S1, S2) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision. <end_of_turn>" |
| (S2, S1) | "The twin-engine commercial jetliner taxiing at the time, Flight Alpha-9, caused the runway collision. <end_of_turn>" |
| (S1, S3) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test. <end_of_turn>" |
| (S3, S1) | "Flight Alpha-9 caused the runway collision during a simulator test. <end_of_turn>" |
| (S2, S3) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test. <end_of_turn>" |
| (S3, S2) | "Flight Alpha-9 caused the runway collision during a simulator test. <end_of_turn>" |
| (S1, S2, S3) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test. <end_of_turn>" |
| (S1, S3, S2) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision during a simulator test. <end_of_turn>" |
| (S2, S1, S3) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test. <end_of_turn>" |
| (S2, S3, S1) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the minor runway collision during a simulator test. <end_of_turn>" |
| (S3, S1, S2) | "Flight Alpha-9 caused the runway collision during a simulator test. <end_of_turn>" |
| (S3, S2, S1) | "Flight Alpha-9 caused the runway collision. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -2.5981 | 13.7027 | 15.9996 | -0.0959 | 0.5056 | 0.5903 |
| BERT Similarity | 0.2167 | 0.2691 | 0.3377 | 0.2631 | 0.3268 | 0.4101 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A twin-engine commercial jetliner caused the runway collision."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1156 |
| \{S1\} | -6.6016 | 0.7879 | 0.9035 |
| \{S2\} | 25.9141 | 0.8139 | 0.9295 |
| \{S3\} | -4.7734 | 0.7884 | 0.9040 |
| \{S1, S2\} | 25.8750 | 0.8172 | 0.9328 |
| \{S1, S3\} | -5.6406 | 0.7884 | 0.9040 |
| \{S2, S3\} | 26.7656 | 0.8601 | 0.9757 |
| \{S1, S2, S3\} | 26.7422 | 0.8458 | 0.9613 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The twin-engine commercial jetliner caused the runway collision. <end_of_turn>" |
| (S2) | "Flight Alpha-9, the only twin-engine commercial jetliner taxiing, caused the runway collision. <end_of_turn>" |
| (S3) | "A twin-engine commercial jetliner caused the runway collision. <end_of_turn>" |
| (S1, S2) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision. <end_of_turn>" |
| (S2, S1) | "The twin-engine commercial jetliner taxiing at the time, Flight Alpha-9, caused the runway collision. <end_of_turn>" |
| (S1, S3) | "A twin-engine commercial jetliner caused the runway collision. <end_of_turn>" |
| (S3, S1) | "A twin-engine commercial jetliner caused the runway collision. <end_of_turn>" |
| (S2, S3) | "Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time, caused the runway collision. <end_of_turn>" |
| (S3, S2) | "Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time, caused the runway collision. <end_of_turn>" |
| (S1, S2, S3) | "A twin-engine commercial jetliner caused the runway collision. Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time. <end_of_turn>" |
| (S1, S3, S2) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision. <end_of_turn>" |
| (S2, S1, S3) | "A twin-engine commercial jetliner caused the runway collision. Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time. <end_of_turn>" |
| (S2, S3, S1) | "A twin-engine commercial jetliner caused the runway collision. Flight Alpha-9 was the only twin-engine commercial jetliner taxiing at the time. <end_of_turn>" |
| (S3, S1, S2) | "Flight Alpha-9, a twin-engine commercial jetliner, caused the runway collision. <end_of_turn>" |
| (S3, S2, S1) | "Flight Alpha-9, the only twin-engine commercial jetliner taxiing at the time, caused the runway collision. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -2.3594 | 30.1016 | -1.0000 | -0.0882 | 1.1256 | -0.0374 |
| BERT Similarity | 0.2584 | 0.3072 | 0.2801 | 0.3055 | 0.3633 | 0.3312 |

---

### Example 12: Astronomy / Telescope

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `-0.0839`

#### Metadata
- **Question**: *"Which instrument discovered the distant exoplanet?"*
- **Target Response**: *"The Kepler satellite discovered the exoplanet."*
- **S1 (Logical premise 1)**: *"The exoplanet was detected by a space-based transit-photometry telescope."*
- **S2 (Logical premise 2)**: *"The only space-based transit-photometry telescope active during the mission was the Kepler satellite."*
- **S3a (Adversarial Distractor)**: *"Radio telescopes on Earth detect emissions from distant pulsars and quasars."*
- **S3b (Syntactic Distractor)**: *"The Kepler satellite was deactivated after its fuel supply ran out."*
- **S3c (Semantic Distractor)**: *"A space telescope measuring light dips detected the exoplanet."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.5196 >= best(S1,S2)=0.4853 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.3057 <= worst(S1,S2)=0.2982 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3050 >= best(S1,S2)=0.3965 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.0115 <= worst(S1,S2)=-0.0307 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Radio telescopes on Earth detect emissions from distant pulsars and quasars."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.0978 |
| \{S1\} | -2.2734 | 0.7153 | 0.8131 |
| \{S2\} | 13.2422 | 0.8926 | 0.9904 |
| \{S3\} | -8.6094 | 0.5583 | 0.6561 |
| \{S1, S2\} | 15.3594 | 0.8353 | 0.9331 |
| \{S1, S3\} | -2.4648 | 0.6973 | 0.7951 |
| \{S2, S3\} | 14.6641 | 0.8362 | 0.9340 |
| \{S1, S2, S3\} | 15.2031 | 0.7903 | 0.8881 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The exoplanet was discovered by a space-based transit-photometry telescope. <end_of_turn>" |
| (S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to observe the planet. <end_of_turn>" |
| (S3) | "The context does not state which instrument discovered a distant exoplanet. It only mentions radio telescopes used to detect emissions from pulsars and quasars. <end_of_turn>" |
| (S1, S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet. <end_of_turn>" |
| (S2, S1) | "The exoplanet was discovered by the Kepler satellite. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S1, S3) | "A space-based transit-photometry telescope discovered the distant exoplanet. Radio telescopes are used to detect emissions from pulsars and quasars. <end_of_turn>" |
| (S3, S1) | "The exoplanet was discovered by a space-based transit-photometry telescope. Radio telescopes on Earth are used to detect emissions from pulsars and quasars. <end_of_turn>" |
| (S2, S3) | "The Kepler satellite discovered the distant exoplanet. It is a space-based transit-photometry telescope. <end_of_turn>" |
| (S3, S2) | "The Kepler satellite, a space-based transit-photometry telescope, discovered the distant exoplanet. <end_of_turn>" |
| (S1, S2, S3) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet. <end_of_turn>" |
| (S1, S3, S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet. <end_of_turn>" |
| (S2, S1, S3) | "The exoplanet was discovered by a space-based transit-photometry telescope. The Kepler satellite was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S2, S3, S1) | "The exoplanet was discovered by the Kepler satellite. It is the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S3, S1, S2) | "The exoplanet was discovered by the Kepler satellite. It is a space-based transit-photometry telescope. <end_of_turn>" |
| (S3, S2, S1) | "The exoplanet was discovered by the Kepler satellite. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 0.7988 | 17.1211 | -2.7168 | 0.0525 | 1.1262 | -0.1787 |
| BERT Similarity | 0.2367 | 0.3948 | 0.1587 | 0.2995 | 0.4996 | 0.2008 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"The Kepler satellite was deactivated after its fuel supply ran out."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.0978 |
| \{S1\} | -2.2734 | 0.7153 | 0.8131 |
| \{S2\} | 13.2422 | 0.8926 | 0.9904 |
| \{S3\} | 14.8203 | 0.7645 | 0.8623 |
| \{S1, S2\} | 15.3594 | 0.8353 | 0.9331 |
| \{S1, S3\} | 14.8086 | 0.8232 | 0.9210 |
| \{S2, S3\} | 13.9492 | 0.7976 | 0.8954 |
| \{S1, S2, S3\} | 14.9492 | 0.7746 | 0.8724 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The exoplanet was discovered by a space-based transit-photometry telescope. <end_of_turn>" |
| (S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to observe the planet. <end_of_turn>" |
| (S3) | "The Kepler satellite discovered the distant exoplanet. <end_of_turn>" |
| (S1, S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet. <end_of_turn>" |
| (S2, S1) | "The exoplanet was discovered by the Kepler satellite. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S1, S3) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet. <end_of_turn>" |
| (S3, S1) | "The exoplanet was discovered by the Kepler satellite. It was a space-based transit-photometry telescope. <end_of_turn>" |
| (S2, S3) | "The Kepler satellite discovered the distant exoplanet. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S3, S2) | "The Kepler satellite discovered the distant exoplanet. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S1, S2, S3) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet. <end_of_turn>" |
| (S1, S3, S2) | "The Kepler satellite discovered the distant exoplanet. It was the only active space-based transit-photometry telescope during the mission. <end_of_turn>" |
| (S2, S1, S3) | "The exoplanet was discovered by the Kepler satellite. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S2, S3, S1) | "The exoplanet was discovered by the Kepler satellite. <end_of_turn>" |
| (S3, S1, S2) | "The Kepler satellite discovered the distant exoplanet. It was the only active space-based transit-photometry telescope during the mission. <end_of_turn>" |
| (S3, S2, S1) | "The exoplanet was discovered by the Kepler satellite. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.0736 | 7.2546 | 7.7682 | -0.0049 | 0.4853 | 0.5196 |
| BERT Similarity | 0.2310 | 0.3069 | 0.2368 | 0.2982 | 0.3962 | 0.3057 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A space telescope measuring light dips detected the exoplanet."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1189 |
| \{S1\} | -2.2734 | 0.7104 | 0.8293 |
| \{S2\} | 13.2422 | 0.7894 | 0.9083 |
| \{S3\} | -3.3359 | 0.6985 | 0.8175 |
| \{S1, S2\} | 15.3594 | 0.7754 | 0.8943 |
| \{S1, S3\} | -3.6055 | 0.7232 | 0.8421 |
| \{S2, S3\} | 17.0703 | 0.7973 | 0.9162 |
| \{S1, S2, S3\} | 16.8672 | 0.7812 | 0.9001 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The exoplanet was discovered by a space-based transit-photometry telescope. <end_of_turn>" |
| (S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to observe the planet. <end_of_turn>" |
| (S3) | "A space telescope discovered the distant exoplanet. <end_of_turn>" |
| (S1, S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet. <end_of_turn>" |
| (S2, S1) | "The exoplanet was discovered by the Kepler satellite. It was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S1, S3) | "The exoplanet was discovered by a space-based transit-photometry telescope. <end_of_turn>" |
| (S3, S1) | "A space-based transit-photometry telescope discovered the distant exoplanet. <end_of_turn>" |
| (S2, S3) | "The Kepler satellite, a space-based transit-photometry telescope, discovered the distant exoplanet. <end_of_turn>" |
| (S3, S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the light dips caused by the planet passing in front of its star. <end_of_turn>" |
| (S1, S2, S3) | "The Kepler satellite discovered the distant exoplanet. A space telescope measuring light dips detected the exoplanet. <end_of_turn>" |
| (S1, S3, S2) | "The Kepler satellite discovered the distant exoplanet. It detected the exoplanet using space-based transit-photometry. <end_of_turn>" |
| (S2, S1, S3) | "The exoplanet was discovered by the Kepler satellite. It is the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S2, S3, S1) | "The exoplanet was discovered by a space-based transit-photometry telescope. The Kepler satellite was the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |
| (S3, S1, S2) | "The Kepler satellite discovered the distant exoplanet. It used transit-photometry to detect the planet by measuring dips in light. <end_of_turn>" |
| (S3, S2, S1) | "The exoplanet was discovered by the Kepler satellite. It is the only space-based transit-photometry telescope active during the mission. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.5176 | 17.5781 | -0.1934 | -0.0307 | 1.0421 | -0.0115 |
| BERT Similarity | 0.2332 | 0.3097 | 0.2382 | 0.2985 | 0.3965 | 0.3050 |

---

### Example 13: Music / Era

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.0508`

#### Metadata
- **Question**: *"Which composer wrote the symphony?"*
- **Target Response**: *"Ludwig van Beethoven wrote the symphony."*
- **S1 (Logical premise 1)**: *"The musical piece was composed by a deaf German master transitioning from Classical to Romantic."*
- **S2 (Logical premise 2)**: *"The only deaf German composer transitioning between those eras was Ludwig van Beethoven."*
- **S3a (Adversarial Distractor)**: *"Wolfgang Amadeus Mozart was a prolific child prodigy of the Classical era."*
- **S3b (Syntactic Distractor)**: *"Ludwig van Beethoven composed nine complete symphonies in his lifetime."*
- **S3c (Semantic Distractor)**: *"A deaf German composer transitioning from Classical to Romantic wrote the symphony."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.4042 >= best(S1,S2)=0.4730 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.2230 <= worst(S1,S2)=0.3777 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3366 >= best(S1,S2)=0.3938 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=0.0640 <= worst(S1,S2)=0.0860 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"Wolfgang Amadeus Mozart was a prolific child prodigy of the Classical era."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1106 |
| \{S1\} | 2.5000 | 0.5828 | 0.6933 |
| \{S2\} | 6.2188 | 0.7504 | 0.8610 |
| \{S3\} | -7.7812 | 0.4399 | 0.5504 |
| \{S1, S2\} | 7.1562 | 0.7757 | 0.8862 |
| \{S1, S3\} | 1.0234 | 0.5652 | 0.6758 |
| \{S2, S3\} | 3.8281 | 0.5015 | 0.6120 |
| \{S1, S2, S3\} | 5.8281 | 0.7131 | 0.8237 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The symphony was composed by a deaf German master. <end_of_turn>" |
| (S2) | "Ludwig van Beethoven was the deaf German composer. <end_of_turn>" |
| (S3) | "The context does not provide information about which composer wrote a symphony. <end_of_turn>" |
| (S1, S2) | "Ludwig van Beethoven wrote the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S2, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S1, S3) | "The context states the composer was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S3, S1) | "The symphony was composed by a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S2, S3) | "The context states that Ludwig van Beethoven was the only deaf German composer transitioning between eras. Therefore, Beethoven wrote the symphony. <end_of_turn>" |
| (S3, S2) | "The context does not provide information about which composer wrote a symphony. <end_of_turn>" |
| (S1, S2, S3) | "Ludwig van Beethoven wrote the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S1, S3, S2) | "The symphony was written by Ludwig van Beethoven. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S2, S1, S3) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S2, S3, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S3, S1, S2) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic music. <end_of_turn>" |
| (S3, S2, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 3.1237 | 6.3854 | -3.6810 | 0.5360 | 1.0956 | -0.6316 |
| BERT Similarity | 0.2899 | 0.3418 | 0.0814 | 0.4065 | 0.4794 | 0.1141 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"Ludwig van Beethoven composed nine complete symphonies in his lifetime."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.1106 |
| \{S1\} | 2.5000 | 0.5828 | 0.6933 |
| \{S2\} | 6.2188 | 0.7504 | 0.8610 |
| \{S3\} | 6.9219 | 0.4952 | 0.6058 |
| \{S1, S2\} | 7.1562 | 0.7757 | 0.8862 |
| \{S1, S3\} | 5.5547 | 0.7599 | 0.8705 |
| \{S2, S3\} | 6.4062 | 0.6256 | 0.7361 |
| \{S1, S2, S3\} | 6.5260 | 0.7682 | 0.8787 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The symphony was composed by a deaf German master. <end_of_turn>" |
| (S2) | "Ludwig van Beethoven was the deaf German composer. <end_of_turn>" |
| (S3) | "Ludwig van Beethoven composed nine complete symphonies in his lifetime. <end_of_turn>" |
| (S1, S2) | "Ludwig van Beethoven wrote the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S2, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S1, S3) | "Ludwig van Beethoven composed the symphony. He was a deaf German master transitioning from Classical to Romantic music. <end_of_turn>" |
| (S3, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S2, S3) | "Ludwig van Beethoven, a deaf German composer, wrote nine complete symphonies. <end_of_turn>" |
| (S3, S2) | "Ludwig van Beethoven composed nine complete symphonies in his lifetime. <end_of_turn>" |
| (S1, S2, S3) | "Ludwig van Beethoven wrote the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S1, S3, S2) | "Ludwig van Beethoven composed the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S2, S1, S3) | "Ludwig van Beethoven composed the symphony. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S2, S3, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S3, S1, S2) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic music. <end_of_turn>" |
| (S3, S2, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 0.8016 | 3.0868 | 2.6376 | 0.1228 | 0.4730 | 0.4042 |
| BERT Similarity | 0.2901 | 0.3068 | 0.1713 | 0.3777 | 0.3993 | 0.2230 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A deaf German composer transitioning from Classical to Romantic wrote the symphony."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.3151 |
| \{S1\} | 2.5000 | 0.2600 | 0.5751 |
| \{S2\} | 6.2188 | 0.2748 | 0.5898 |
| \{S3\} | 1.5469 | 0.2534 | 0.5684 |
| \{S1, S2\} | 7.1562 | 0.3788 | 0.6939 |
| \{S1, S3\} | 0.1484 | 0.3457 | 0.6608 |
| \{S2, S3\} | 7.7812 | 0.4494 | 0.7644 |
| \{S1, S2, S3\} | 7.4297 | 0.4770 | 0.7921 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer the question. <end_of_turn>" |
| (S1) | "The symphony was composed by a deaf German master. <end_of_turn>" |
| (S2) | "Ludwig van Beethoven was the deaf German composer. <end_of_turn>" |
| (S3) | "The symphony was written by a deaf German composer. <end_of_turn>" |
| (S1, S2) | "Ludwig van Beethoven wrote the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S2, S1) | "The symphony was composed by Ludwig van Beethoven. He was a deaf German master transitioning from Classical to Romantic. <end_of_turn>" |
| (S1, S3) | "A deaf German composer transitioning from Classical to Romantic wrote the symphony. <end_of_turn>" |
| (S3, S1) | "The symphony was written by a deaf German composer. <end_of_turn>" |
| (S2, S3) | "Ludwig van Beethoven wrote the symphony. He was a deaf German composer transitioning from Classical to Romantic. <end_of_turn>" |
| (S3, S2) | "Ludwig van Beethoven wrote the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S1, S2, S3) | "Ludwig van Beethoven wrote the symphony. <end_of_turn>" |
| (S1, S3, S2) | "Ludwig van Beethoven wrote the symphony. <end_of_turn>" |
| (S2, S1, S3) | "The symphony was written by Ludwig van Beethoven. He was a deaf German composer transitioning from Classical to Romantic. <end_of_turn>" |
| (S2, S3, S1) | "The symphony was written by Ludwig van Beethoven. He was a deaf German composer transitioning from Classical to Romantic. <end_of_turn>" |
| (S3, S1, S2) | "Ludwig van Beethoven wrote the symphony. He was the only deaf German composer transitioning from Classical to Romantic music. <end_of_turn>" |
| (S3, S2, S1) | "The symphony was written by Ludwig van Beethoven. He was the only deaf German composer transitioning between the Classical and Romantic eras. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | 0.6393 | 6.3151 | 0.4753 | 0.0860 | 0.8500 | 0.0640 |
| BERT Similarity | 0.1286 | 0.1878 | 0.1606 | 0.2696 | 0.3938 | 0.3366 |

---

### Example 14: Sociology / Theory

#### Example Summary
- **Overall Status**: ✅ **PASSED ALL CHECKS**
- **Diagnostic Quality Score**: `0.4093`

#### Metadata
- **Question**: *"Which sociological concept explained the rapid spread of the rumor?"*
- **Target Response**: *"The contagion theory explained the rumor's spread."*
- **S1 (Logical premise 1)**: *"The collective behavior was explained by a framework stating that crowd emotions are highly infectious and spread rapidly."*
- **S2 (Logical premise 2)**: *"The only framework stating that crowd emotions are highly infectious and spread rapidly is the contagion theory."*
- **S3a (Adversarial Distractor)**: *"The bystander effect describes how individuals are less likely to offer help when other people are present."*
- **S3b (Syntactic Distractor)**: *"The contagion theory was first proposed in the context of nineteenth-century crowd psychology."*
- **S3c (Semantic Distractor)**: *"A framework stating that crowd emotions are highly infectious and spread rapidly explained the collective behavior."*

#### Diagnostic Rule Status
1. ✅ **Rule 1**: All values within [-1.5, 1.5]
2. ✅ **Rule 2**: Case B ULL fooled: S3=0.7362 >= best(S1,S2)=0.4083 - 0.15
3. ✅ **Rule 3**: Case B BERT not fooled: S3=0.3138 <= worst(S1,S2)=0.3284 + 0.15
4. ✅ **Rule 4**: Case C BERT fooled: S3=0.3261 >= best(S1,S2)=0.3478 - 0.15
5. ✅ **Rule 5**: Case C ULL not fooled: S3=-0.2507 <= worst(S1,S2)=-0.1622 + 0.15

#### Case A (Adversarial Distractor)
Distractor ($S_3$): *"The bystander effect describes how individuals are less likely to offer help when other people are present."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.0810 |
| \{S1\} | -4.3828 | 0.8757 | 0.9568 |
| \{S2\} | 4.3906 | 0.9087 | 0.9897 |
| \{S3\} | -10.1250 | 0.5830 | 0.6640 |
| \{S1, S2\} | 4.4688 | 0.9087 | 0.9897 |
| \{S1, S3\} | -7.4531 | 0.8829 | 0.9639 |
| \{S2, S3\} | 1.1406 | 0.9003 | 0.9814 |
| \{S1, S2, S3\} | 2.5820 | 0.9064 | 0.9874 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor. <end_of_turn>" |
| (S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3) | "The provided context does not mention a rumor or explain its spread. <end_of_turn>" |
| (S1, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S2, S1) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S1, S3) | "The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor. <end_of_turn>" |
| (S3, S1) | "The sociological concept that explained the rapid spread of the rumor is the idea that crowd emotions are highly infectious and spread rapidly. <end_of_turn>" |
| (S2, S3) | "The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious. <end_of_turn>" |
| (S3, S2) | "The sociological concept that explained the rapid spread of the rumor is the contagion theory. This theory states that crowd emotions are highly infectious and spread rapidly. <end_of_turn>" |
| (S1, S2, S3) | "The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious and spread rapidly. <end_of_turn>" |
| (S1, S3, S2) | "The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious and spread rapidly. <end_of_turn>" |
| (S2, S1, S3) | "The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious. <end_of_turn>" |
| (S2, S3, S1) | "The sociological concept that explained the rapid spread of the rumor is the contagion theory. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S1, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S2, S1) | "The sociological concept that explained the rapid spread of the rumor is the contagion theory. This theory posits that crowd emotions are highly infectious and spread rapidly. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -0.5221 | 8.1615 | -5.0573 | -0.2022 | 3.1609 | -1.9586 |
| BERT Similarity | 0.3439 | 0.3691 | 0.1934 | 0.3794 | 0.4072 | 0.2133 |

#### Case B (Syntactic Distractor)
Distractor ($S_3$): *"The contagion theory was first proposed in the context of nineteenth-century crowd psychology."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.0838 |
| \{S1\} | -4.3828 | 0.8571 | 0.9409 |
| \{S2\} | 4.3906 | 0.9162 | 1.0000 |
| \{S3\} | 6.1250 | 0.8554 | 0.9391 |
| \{S1, S2\} | 4.4688 | 0.9162 | 1.0000 |
| \{S1, S3\} | 7.4531 | 0.8964 | 0.9802 |
| \{S2, S3\} | 6.6328 | 0.8914 | 0.9752 |
| \{S1, S2, S3\} | 7.1953 | 0.9161 | 0.9998 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor. <end_of_turn>" |
| (S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3) | "The contagion theory, first proposed in the context of nineteenth-century crowd psychology, explains the rapid spread of the rumor. <end_of_turn>" |
| (S1, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S2, S1) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S1, S3) | "The sociological concept of contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S1) | "The contagion theory, which posits that crowd emotions are highly infectious and spread rapidly, explained the rumor's quick dissemination. <end_of_turn>" |
| (S2, S3) | "The contagion theory, which posits that crowd emotions are highly infectious and spread rapidly, explains the rumor's quick dissemination. <end_of_turn>" |
| (S3, S2) | "The contagion theory explained the rapid spread of the rumor because it states that crowd emotions are highly infectious and spread rapidly. <end_of_turn>" |
| (S1, S2, S3) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S1, S3, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S2, S1, S3) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S2, S3, S1) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S1, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S2, S1) | "The contagion theory explained the rapid spread of the rumor. This theory states that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.0391 | 2.9375 | 5.2969 | -0.1444 | 0.4083 | 0.7362 |
| BERT Similarity | 0.3008 | 0.3278 | 0.2875 | 0.3284 | 0.3578 | 0.3138 |

#### Case C (Semantic Distractor)
Distractor ($S_3$): *"A framework stating that crowd emotions are highly infectious and spread rapidly explained the collective behavior."*

##### Subset Characteristic Function Values

| Subset $S$ | Unweighted LL $v(S)$ | BERT Similarity $v(S)$ | Raw BERT Similarity |
| :--- | :---: | :---: | :---: |
| $\emptyset$ | 0.0000 | 0.0000 | 0.0544 |
| \{S1\} | -4.3828 | 0.8972 | 0.9516 |
| \{S2\} | 4.3906 | 0.9209 | 0.9754 |
| \{S3\} | -5.7891 | 0.8972 | 0.9516 |
| \{S1, S2\} | 4.4688 | 0.9209 | 0.9754 |
| \{S1, S3\} | -6.6484 | 0.9046 | 0.9591 |
| \{S2, S3\} | 4.7422 | 0.9209 | 0.9754 |
| \{S1, S2, S3\} | 6.4010 | 0.9250 | 0.9795 |

##### Model Generated Responses for All Subsets

| Subset Permutation | Generated Response |
| :--- | :--- |
| Empty context | "Please provide the context so I can answer your question. <end_of_turn>" |
| (S1) | "The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor. <end_of_turn>" |
| (S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3) | "The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor. <end_of_turn>" |
| (S1, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S2, S1) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S1, S3) | "The sociological concept that explained the rapid spread of the rumor is that crowd emotions are highly infectious and spread rapidly. <end_of_turn>" |
| (S3, S1) | "The sociological concept of **highly infectious crowd emotions** explained the rapid spread of the rumor. <end_of_turn>" |
| (S2, S3) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S1, S2, S3) | "The sociological concept that explained the rapid spread of the rumor is the contagion theory. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S1, S3, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S2, S1, S3) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S2, S3, S1) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S1, S2) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |
| (S3, S2, S1) | "The contagion theory explained the rapid spread of the rumor. This theory posits that crowd emotions are highly infectious and spread quickly. <end_of_turn>" |

##### Shapley Context Attribution Results

| Method | S1 ($\phi_1$) | S2 ($\phi_2$) | S3 ($\phi_3$) | S1 ($\phi_{\text{norm}, 1}$) | S2 ($\phi_{\text{norm}, 2}$) | S3 ($\phi_{\text{norm}, 3}$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Unweighted LL | -1.0382 | 9.0438 | -1.6046 | -0.1622 | 1.4129 | -0.2507 |
| BERT Similarity | 0.3017 | 0.3217 | 0.3017 | 0.3261 | 0.3478 | 0.3261 |

---

