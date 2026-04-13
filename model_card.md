# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
MusicMatch   

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

- The model matches music to different user preferences
- Matches based on genre, energy, etc
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Weighted based on genres (3), energy (2), mood (2), and acoustics (1). Higher priority on genres
---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

- 18 songs in the catalog
- Genres include: pop, lofi, rock, intense, ambient, jazz, synthwave, etc
- Data was added based on real songs
- Small dataset: likely missing data
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

- Simple and fast recommendations
- Matching similar genres with profiles
- Correctly determines good recommendations for songs
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The system over prioritizes genre because of its higher weight. It is using the settings that were specifically mentioned in the csv and is relying on that specific data. It is only comparing recommendations based on 4 factors and can only recommend the specific songs in the dataset.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

- Pop fan was suggested pop genre preferences
- lofi acoustic lover was given low energy songs
- metal rock fan suggested intense metal songs
- peaceful minimalist given classical peaceful prefernces
- Dark energetic fan suggested synth pulse music
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

- Add more data to the dataset
- Create higher criteria recommendations
- handle generic prompts or matched taste based on songs users listen to
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

- recommender systems aren't too complicated to create
- Surprised on the different ways recommendation systems are made
- makes me respect good algorithmic recommendations