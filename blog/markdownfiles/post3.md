# What 2am banana bread can tell us about software engineering

Lying awake at 2am, unable to sleep and smelling the bananas in the kitchen getting spottier by the minute, I did what any reasonable person would do and attempted to make banana bread. Attempted, of course, because articles are rarely written when something mundane goes as expected.

Banana bread is a relatively easy recipe. A recipe that I had done dozens of times before. However when I checked it 30 minutes after it had gone in the oven everything was not right. Obviously a mistake had been made.

And herein is the first lesson - constant monitoring, and alerting when something isn’t right. In the case of banana bread it’s too late to go back and modify the ingredients, but when running software a sudden increase in volume can be the indication that it’s just about to ~~flop~~ crash. 

Bread is expected to rise, but only because you know that ofcourse it will! But if it was the first time you had ever set foot in a kitchen, would you be able to tell if it was normal or an indication of a pending calamity? This is the same for metrics; you need to understand the system before you can tell when something is unusual.

So as soon as I was alerted that something was wrong, it was time to debug. Unfortunately an oven door stood between the problem and me, which was vaguely reminiscent of attempting to debug a remote host with nothing more than a VNC connection to a machine several continents, and several seconds, away. 

Since running hands-on diagnostics was out of the question, my only option was to turn to the documentation. And this is where the second lesson comes in. When you do a process enough it becomes repetitive, and when you stop paying attention and that is when the mistakes creep in. 

> “It is possible to commit no mistakes and still lose. That is not a weakness; that is life.” Jean Luc Picard, caption: in this instance clearly I committed a mistake, but I like this quote nevertheless>

When I baked my first loaf I followed the recipe exactly. I carefully measured the ingredients, set the temperature just right, and double checked each step. But after getting familiar with the process I started to rely on the recipe less and less. Research shows that checklists improve outcomes. Doctors and pilots use them, and so should we.

Going back to the recipe it became immediately obvious that I had missed a crucial ingredient. Now to simply put the fix into production...

This is the third lesson. Understand the remediation steps to a problem, and clearly communicate with your stakeholders about the process. In this case I patiently told my stomach that it will probably not get exactly what was promised - it will have bananas and will be some sort of bread, but it will just have to finish baking before we can check. 

And sometimes solving problems takes time, and sometimes there is nothing you can do about that. If a server is restarting there is no amount of bash magic to make the platters spin faster or the network interface to come up sooner, but the one thing you can control is the expectations. 

## Whilst chewing on the brick of regret, I had a lot of time to reflect

Because each failure is a learning opportunity, and a good postmortem is about identifying the faults in the system and not assigning blame. It would be easy to say that because it was 2am and I was already sleep-deprived that it was a bad idea to start baking, however a better approach would be to ask how was it possible that the mistake was made, and how it could be avoided in the future? What factors lead to the situation?

I skipped the checklist because I was overconfident. I missed the ingredients because they were not stored together. I was making banana bread at 2am because I wasn’t better prepared by making it earlier in the night.

I fixed it by..
In this case I wrote out the recipe and tacked it to the cupboard where I store the baking ingredients so that it would always be immediately visible. and I moved the baking powder to the same shelf as the flour, as they would always be used together.
