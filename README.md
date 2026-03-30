# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world recommenders like Spotify combine collaborative filtering (learning from millions of users with similar taste) and content-based filtering (analyzing the actual properties of each song). My version focuses on content-based filtering: it compares the attributes of each song directly against what the user says they prefer, without relying on any other users' behavior. For each song, the system computes a proximity score — the closer a song's attributes are to the user's preferences, the higher it scores. After scoring every song in the catalog, the system ranks them and returns the top matches. This approach is transparent and easy to reason about, which makes it a good starting point before adding more complex signals.

### Song Features

Each `Song` object stores the following attributes used in scoring:

- `energy` — how intense or active the track feels (0.0 to 1.0)
- `acousticness` — how acoustic vs. electronic the song is (0.0 to 1.0)
- `valence` — emotional positivity; high = uplifting, low = melancholic (0.0 to 1.0)
- `danceability` — how suitable the track is for dancing (0.0 to 1.0)
- `genre` — broad style category (pop, lofi, rock, ambient, jazz, synthwave, indie pop)
- `mood` — descriptive feel of the track (happy, chill, intense, relaxed, moody, focused)
- `tempo_bpm` — beats per minute (stored but not weighted heavily at this scale)

### UserProfile Features

Each `UserProfile` stores:

- `target_energy` — the user's preferred energy level (0.0 to 1.0)
- `likes_acoustic` — whether the user prefers acoustic over electronic sounds
- `favorite_genre` — the genre the user most wants to hear
- `favorite_mood` — the mood the user is currently in

### Scoring Rule (per song)

Each numeric feature gets a proximity score: `1 - |user_preference - song_value|`. These are combined using weighted average:

```
total_score = 0.35 × energy_score
            + 0.30 × acousticness_score
            + 0.20 × valence_score
            + 0.15 × danceability_score
```

Categorical matches (genre, mood) add a small bonus on top.

### Ranking Rule (across all songs)

All songs are scored, then sorted by `total_score` descending. The top `k` songs (default 5) are returned as recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:

- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:

- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:

- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"
```
