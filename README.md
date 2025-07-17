# CRISPR Patent Text Analysis

This is a small text analysis project focused on identifying the most frequent and meaningful terms in patent abstracts and titles related to CRISPR technology.

The project cleans and preprocesses the text data, removes common stopwords and uninformative terms, and finally visualizes the top 30 most frequent words using a bar chart.

---

## 🧪 Project Purpose

The goal of this project is to:

- Combine title and abstract information from CRISPR-related patents.
- Preprocess the text (lowercasing, removing punctuation, filtering stopwords).
- Extract and visualize frequently used terms after cleaning.
- Understand key vocabulary and trends in CRISPR patent literature.

---

## 📁 Dataset

The dataset used is ``, which includes CRISPR-related patents with at least title and abstract fields.

> **Source:** The dataset was downloaded from a public data repository. We did not collect or scrape this data programmatically. Please refer to the original source for licensing and usage rights.

If you're using a specific site like **Lens.org**, **PatentsView**, **Google Patents**, or **NCBI**, specify it:

> Source: [Lens.org](https://www.lens.org/)

---

## 📦 Requirements

This project uses the following Python libraries:

- `pandas`
- `re`
- `collections.Counter`
- `matplotlib`

You can install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

```bash
python crispr_text_analysis.py
```

The script will output the most common cleaned words in the terminal and display a bar chart of the top 30 terms.

---

## 📊 Output Example

```
[('rna', 152), ('nuclease', 137), ('guide', 124), ('sequence', 118), ...]
```



---

## 📄 License

This project is shared for educational and non-commercial purposes.\
Please respect the license of the original dataset if you use it further.

---

## 🤝 Contributions

This is a learning project. Contributions and suggestions are welcome!

