<h1><b>SpellChecker Project</b></h1>

<h1><b>Overview</b></h1>

The SpellChecker Project is a multi-phase initiative aimed at developing a robust and user-friendly tool for spelling corrections. Beginning with a basic word-check mechanism, it evolved to identify and suggest corrections for misspellings, and finally expanded to check complete sentences.

<h2>Table of Contents</h2>

<b>Phase 1: Initial Spellcheck with Limited Dictionary</b><br>
<b>Phase 2: Suggestion Mechanism</b><br>
<b>Phase 3: Expanded Dictionary and Testing</b><br>
<b>Phase 4: Sentence-Level Spellcheck</b><br>
<b>Testing Strategy</b><br>
<a name="phase-1"></a>

<h3><b>Phase 1: Initial Spellcheck with Limited Dictionary</b></h3>

This phase marked the inception of the project. The spellchecker started with a rudimentary approach, relying on a confined dictionary that primarily included names of fruits. Users inputted a word and the system verified its spelling based on this restricted set. Words not present in the dictionary were flagged as potentially misspelled.

<a name="phase-2"></a>

<h3><b>Phase 2: Suggestion Mechanism</b></h3>

Building on Phase 1, this phase introduced the functionality to provide suggestions for misspellings. By leveraging the concept of the Levenshtein distance—a measure of similarity between two strings—the system could offer the closest matches from the dictionary as suggestions, making the spellcheck experience more interactive and helpful.

<a name="phase-3"></a>

<h3><b>Phase 3: Expanded Dictionary and Testing</b></h3>

With the aim of enhancing accuracy, this phase expanded the dictionary manifold by transitioning from a mere list of words to an SQLite database. This comprehensive dictionary allowed the spellchecker to cross-check inputs against a much broader database and offer a more diverse set of suggestions. In tandem with this expansion, testing scripts were introduced to gauge the efficiency and precision of the system, facilitating iterative improvements.

<a name="phase-4"></a>

<h3><b>Phase 4: Sentence-Level Spellcheck</b></h3>

While previous phases targeted individual words, Phase 4 saw the evolution of the system to check entire sentences for spelling errors. This comprehensive approach ensured that users received feedback not just on isolated words but on their entire input, making the tool more practical for daily usage.

<a name="testing"></a>

<h3><b>Testing Strategy</b></h3>

Throughout its development, the spellchecker's reliability was ensured through rigorous testing. For the initial phases, the test.py script was employed to evaluate the accuracy of word-level suggestions. As the project progressed to sentence-level checking in Phase 4, the test4.py script was harnessed, using Python's unittest framework. This layered testing ensured that the spellchecker was adept at both detecting misspellings and offering apt corrections.
