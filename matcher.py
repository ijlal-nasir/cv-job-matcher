import textract
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def pdf_to_text(file_path):
  text = str(textract.process(file_path), 'UTF-8').lower()
  return text
  

def match_job(job_data, resume_text):
    job_title = job_data['title']
    job_description = job_data['description']
    job_keywords = job_data['keywords']
    job_df = job_title + job_keywords.replace(",", " ") + job_description
    text_df = [resume_text, job_df]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(text_df)
    cos_similarity = cosine_similarity(count_matrix)[0][1]
    # print('cos_similarity', cos_similarity)
    # print('features', vectorizer.get_feature_names_out())
    return f'{cos_similarity: .2%}'
    