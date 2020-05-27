class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for coef, word in zip(coefs, words):
            result += coef * len(word)
        return result

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for i, coef in enumerate(coefs):
            result += len(words[i]) * coef
        return result
