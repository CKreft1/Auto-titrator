# Auto-titrator
Simple function used as an example of a titration model that could be constructed by students in a chemistry education setting. 

This was my first project after learning python, and it earned me some extra credit in Chemistry.
Composed of 2 functions. The first takes arguments for weak acid concentration, strong base concentration, initial acid volume, and respective pKa values (entered in the form of a list), for acidic protons of a theoretical weak acid. From there, it uses alpha values to determine what volume of base must have been added to reach a given pH. The second function rapidly calls that first function at incrementally increasing pH values and graphs the result.
Weirdly, the graph seems to approach infinity as pH approaches 12, then inverts and becomes negative. Some significant error might be expected at extreme pH values due to activity effects, but approaching infinity is not normal and must be due to some failure of the model. This is "fixed" in the code by limiting the function to below 12.
