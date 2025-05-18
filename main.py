import random
from keybert import KeyBERT
from passage import passages

kw_model = KeyBERT()

def generate_title(text):
    keywords = kw_model.extract_keywords(text, top_n=5, keyphrase_ngram_range=(1, 2))
    if not keywords:
        return "No Title"
    words = [kw[0] for kw in keywords]
    selected = random.sample(words, min(3, len(words)))
    title = ", ".join(selected)
    return title

def create_title_questions(passages):
    questions = []
    answers = []
    for idx, passage in enumerate(passages, 1):
        title = generate_title(passage)
        question = f"Passage {idx}의 제목으로 가장 적절한 것은?\n\n{passage}\n"
        questions.append(question)
        answers.append(f"Passage {idx} 정답: {title}\n")
    return questions, answers

def save_to_file(filename, contents):
    with open(filename, "w", encoding="utf-8") as f:
        for item in contents:
            f.write(item)
            f.write("\n\n")

def main():
    random.seed()  # 매 실행마다 다르게

    questions, answers = create_title_questions(passages)

    save_to_file("title_questions.txt", questions)
    save_to_file("title_answers.txt", answers)

    print("문제와 답안을 각각 title_questions.txt, title_answers.txt에 저장했습니다.")

if __name__ == "__main__":
    main()
