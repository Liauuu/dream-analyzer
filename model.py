import re
import random

STOPWORDS = {
    "the","and","that","with","from","this","have","there","their",
    "your","which","were","when","shall","unto","about","into","such",
    "while","because","although","but","however","so","if","or","nor","yet",
    "on","in","at","by","for","of","to","a","an","is","are","was","be"
}

def extract_keywords(dream_text, max_keywords=6):
    words = re.findall(r"[a-zA-Z]+", dream_text.lower())
    words = [w for w in words if len(w) > 3 and w not in STOPWORDS]
    freq = {}
    for w in words:
        freq[w] = freq.get(w,0)+1
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w,_ in sorted_words[:max_keywords]]

def analyze_dream(dream_text, mood, emotion):
    keywords = extract_keywords(dream_text)

    # mood, emotion도 포함
    extra_keywords = []
    if mood: extra_keywords.extend(m.lower() for m in mood)
    if emotion: extra_keywords.extend(e.lower() for e in emotion)
    keywords.extend(extra_keywords)

    if not keywords:
        return ("📜 Dream Interpretation\n\n"
                "I have carefully read the dream you described.\n"
                "But no clear symbols were found.\n")

    # 🔥 다양한 패턴 (현실+미래+심리+무의식 톤)
    psyche_patterns = [
        "You may be quietly holding onto {kw}, even without realizing it.",
        "At the core of your thoughts lies the influence of {kw}.",
        "Your dream suggests that {kw} is weighing on your emotions.",
        "A hidden part of you still revolves around {kw}.",
        "Your inner self might be struggling with matters tied to {kw}.",
        "Even in waking life, {kw} may echo within your subconscious.",
        "There seems to be an unresolved tension linked with {kw}.",
        "The dream reflects your private concerns about {kw}.",
        "Your mind is still processing feelings related to {kw}.",
        "Deep down, you may feel the presence of {kw} shaping your mood."
    ]

    future_patterns = [
        "Dreams like this sometimes hint that {kw} could shape your future steps.",
        "It may be that {kw} will soon appear as a test in your path.",
        "Such a dream could foreshadow changes involving {kw}.",
        "The theme of {kw} may signal both challenge and opportunity ahead.",
        "It is possible that {kw} will become a turning point in days to come.",
        "Dream interpreters of old would say {kw} suggests an important shift is near.",
        "The vision implies that {kw} may soon demand your attention.",
        "From this dream, one might expect events tied to {kw}.",
        "Your journey could be altered by forces connected to {kw}.",
        "This may indicate that {kw} is a signpost for what lies ahead."
    ]

    unconscious_patterns = [
        "Even if you resist, your inner self resonates with {kw}.",
        "Your subconscious continues to echo with {kw}.",
        "Beneath awareness, {kw} still holds sway.",
        "The hidden layers of your mind speak through {kw}.",
        "Though unnoticed, {kw} pulses through your inner world.",
        "Your unconscious whispers in the form of {kw}.",
        "Behind the veil, {kw} shapes your instincts.",
        "The dream shows your psyche still bound to {kw}.",
        "Part of you you’d rather ignore is expressed by {kw}.",
        "In the silent depth, {kw} remains alive within you."
    ]

    # 랜덤하게 선택
    psyche_lines = [random.choice(psyche_patterns).format(kw=kw) for kw in keywords]
    future_lines = [random.choice(future_patterns).format(kw=kw) for kw in keywords]
    unconscious_lines = [random.choice(unconscious_patterns).format(kw=kw) for kw in keywords]

    output = []
    output.append("📜 Dream Interpretation\n")
    output.append("I have carefully read the dream you described.\n")
    output.append("Here is an interpretation, woven from many voices of old and rephrased for reflection:\n")

    if psyche_lines:
        output.append("Your present psyche:\n- " + "\n- ".join(psyche_lines))
    if unconscious_lines:
        output.append("\nYour unconscious whispers:\n- " + "\n- ".join(unconscious_lines))
    if future_lines:
        output.append("\nPossible future:\n- " + "\n- ".join(future_lines))

    if mood or emotion:
        output.append(f"\nAdditionally, you described the atmosphere as {', '.join(mood) if mood else '-'} "
                      f"and your feelings as {', '.join(emotion) if emotion else '-'}. "
                      "These color the dream’s interpretation.")

    output.append("\nRemember: This is not a fixed prediction, but a reflection for curiosity and self-discovery.")
    return "\n\n".join(output)
