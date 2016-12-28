# GridParser
A Python Script that extracts Structured Data from Praat TextGrids

Praat (a phonetic analysis tool) is often used to label snippets of audio, allowing the user to annotate arbitrary time intervals of audio. Short of writing a Praat script, however, there is no way for users to programatically sift the notes they made on a particular piece of audio. 

The Grid Parser solves this problem by converting a Praat TextGrid (the text file that contains all the user's annotations) to a Python Dictionary. For example, consider the following annotations on a two-channeled audio file:

![Praat Annotation](./Labelling Annotations.png)




