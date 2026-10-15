# PawPal+ Project Reflection

## 1. System Design
- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

The PawPal+ UML design consists of four classes: Owner, Pet, Task, and Scheduler. The Owner class stores the owner's information, availability, and preferences, while the Pet class stores pet details and manages its care tasks. The Task class represents individual activities, including their duration, priority, deadlines, and scheduled times. The Scheduler class coordinates these classes by organizing tasks, checking availability, detecting conflicts, and creating a daily care plan. Together, these classes use object-oriented design principles to make the system organized, reusable, and easy to maintain.

**b. Design changes**

- Did your design change during implementation? no
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I think telling the AI exactly what I need to do and what it needs to generate was key. The incorporated ai into VS did all the work!

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
I let the AI do its thing, and tested it to see if it did what I wanted.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
