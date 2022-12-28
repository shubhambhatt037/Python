score = int(input("Enter your score_> "))

match score:
    case score if score< 30:
        print("Fail")
    case 30:
        print("Pass but bad score")
    case score if score> 40 and score < 50:
        print("Ok")
    case score if score> 50 and score <60:
        print("Ok ok")
    case score if score > 60 and score<75:
        print("First class")
    case score if score > 75:
        print("First class with 'D'")
