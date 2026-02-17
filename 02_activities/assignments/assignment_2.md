# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
    Visualization 1:
    Link: https://public.tableau.com/app/profile/spotify.insights/viz/TheEmojiofSpotifyArtists/DescribeArtists. 
    This interactive Tableau dashboard (“Describe Artists With Emoji”) summarizes which emojis appear most distinctively in playlist titles associated with popular Spotify artists, with filtering by genre/emoji and artist selection. The view is exploratory and intended to reveal associations between artists and commonly used emoji in user-generated playlist titles (data noted as of Feb 2017). 
    I would classify this as a bad visualization because it creates high extraneous cognitive load without delivering clear, accurate comparisons. The chart type is unusual (emoji-as-marks), and viewers must decode what each emoji “means,” then infer what its placement implies. This is a heavy interpretation burden compared to more standard encodings (position/length) that support faster, more accurate reading. Second, the visual encoding is weak for the implied question. The title suggests “describe artists with emoji” and “most distinctive emoji,” but the display doesn’t clearly show *how distinctive* each emoji is (no magnitude, scale, or confidence), and the fixed rank positions (1–10) encourage ordinal reading without a meaningful sense of distance between ranks. This pushes viewers toward approximate interpretation and “pattern guessing,” which increases cognitive load.Third, it’s exploratory and interaction-dependent (filters, clicking emojis) rather than guided. The audience has to navigate the view to learn what matters, which again increases cognitive load and makes the takeaway ambiguous. Finally, the design leans more decorative than analytical. Emojis are culturally loaded and can be interpreted differently across audiences, and they’re not accessibility-friendly (screen readers, small sizes, visual crowding). The overall effect is more “cute dashboard” than a trustworthy, factual presentation. 

    Visualization 2:
    Link: https://public.tableau.com/app/profile/jeehwan/viz/MusicENT_Korea2017/K-PopArtists2019.
    This interactive visualization maps K-Pop artists to one of the “Big 4” Korean agencies (YG, SM, JYP, Big Hit) and links those entities to an outcome metric (YouTube views), with additional categorical cues (e.g., solo vs group, gender). The intent is to support relational exploration-seeing how artists are distributed across agencies while comparing relative visibility/performance via the right-side bar encoding.
    I would classify this as a good visualization because the chart type fits the structure of the data and the likely question. This is fundamentally relational data (agency to artists/groups, plus outcomes like YouTube views), and the flow/connection layout makes those relationships legible in a way that a basic table or single bar chart would not. That fit between purpose and form is a core criterion for effective visualization (purpose, audience, medium). Second, it supports pattern-finding with relatively low extraneous cognitive load: visually tracing which agencies connect to which artists is easier than reading long categorical lists. The design uses Gestalt-style grouping cues (consistent color by agency; continuous lines), so the viewer can follow belongingness and flows without memorizing labels. Third, it’s relatively trustworthy and factual in the way the lecture slides have discuss: it stays 2D, uses clean geometric connectors, and includes a visible source note. Those conventions tend to increase perceived objectivity and credibility, especially when the data source is explicit (provenance rhetoric). 
      ```
    - How could this data visualization have been improved?  
      ```
    Visualization 1:
1) Clarify the analytical goal and encode the key variable explicitly.
   - If the goal is distinctiveness, show a quantitative distinctiveness score (or frequency difference) with a bar chart, dot plot, or heatmap; keep emojis as labels/icons, not the primary data marks. This reduces decoding work and improves comparability. 
2) Make the story more explanatory.
   - Add a short annotation that explains what "distinctive” means, how it was computed, and what the viewer should conclude. This shifts the experience from unguided exploration to guided interpretation.
3) Improve trust and transparency.
   - Include a clear data source/methods note in-view (not hidden in a tab), since provenance signals transparency and increases credibility. 
4) Accessibility.
   - Increase mark size, reduce the number of emojis shown at once (top 3–5), provide text equivalents, and ensure the key comparisons don’t rely on emoji recognition alone.

   Visualization 2:
1) Reduce visual density to lower extraneous cognitive load further.
   - The right-side list and bars are very crowded. Showing fewer artists by default (top N), adding search prominently, or using small multiples by agency would improve readability and keep the viewer from getting lost in a “spaghetti” effect. 
2) Add a clearer explanatory layer.
   - A short annotation (“What to look for”) and a one-sentence definition of what the YouTube metric represents (time window, what’s counted) would guide interpretation and prevent over-reading the graphic as causal or comprehensive. Explanatory guidance reduces the burden on the audience compared to fully self-navigated exploration.
3) Accessibility polish.
   - Ensure the agency colors are colorblind-safe and add redundant encoding (e.g., line pattern or direct labeling) so meaning doesn’t depend on color alone.

      
      ```

- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 01/26/2026`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
