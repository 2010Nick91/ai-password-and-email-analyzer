def password(password):
    from pathlib import Path
    dir = Path(__file__).resolve().parent
    passwordsfile = dir / "spanish_password_elements.txt"
    score = 50
    feedback = {}

    if len(password) < 4:
        score -= 35
        feedback["length"] = "extremely short"
    elif len(password) < 8:
        score -= 15
        feedback["length"] = "very short"
    elif len(password) < 12:
        score +=5
        feedback["length"] = "moderate length"
    elif len(password) < 16:
        score +=15
        feedback["length"] = "good length"
    elif len(password) >= 16:
        score +=20
        feedback["length"] = "excellent length"



    caracters = {}
    if any(c.islower() for c in password):
        caracters["lowercase"] = True
    if any(c.isupper() for c in password):
        caracters["uppercase"] = True
    if any(c.isdigit() for c in password):
        caracters["digits"] = True
    if any(not c.isalnum() for c in password):
        caracters["special"] = True

    variety = len(caracters)
    if variety == 1:
        score -= 10
        feedback["variety"] = "very low"
    elif variety == 2:
        feedback["variety"] = "low"
    elif variety == 3:
        score +=5
        feedback["variety"] = "good"
    elif variety == 4:
        score +=10
        feedback["variety"] = "excellent"


    
    with open(passwordsfile, "r") as f:
        common_passwords = {line.strip() for line in f if line.strip()}
    common_elements_dirty = []
    for element in common_passwords:
        if element.strip() in password.lower():
            common_elements_dirty.append(element.strip())
            score -= 10
            if (len(password) - len(element.strip())) < 4:
                score -= 40
    feedback["common_elements"] = []
    for i in common_elements_dirty:
        is_substring = False
        for k in common_elements_dirty:
            if i != k and i in k:
                is_substring = True
                break
        if not is_substring:
            feedback["common_elements"].append(i)
            
    score = int(round(float(score) * 1.25))

    if score < 0:
        score = 0
    elif score > 100:
        score = 100

    if score == 100:
        feedback["overall"] = "extremely low risk"
    elif score >= 79:
        feedback["overall"] = "low risk"
    elif score >= 59:
        feedback["overall"] = "moderate risk"
    elif score >= 39:
        feedback["overall"] = "high risk"
    elif score == 0:
        feedback["overall"] = "extremely high risk"
    else:
        feedback["overall"] = "very high risk"
    
    score_str = f"{score}/100"
    
    return score, score_str, feedback