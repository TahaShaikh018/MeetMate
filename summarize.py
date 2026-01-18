from pathlib import Path
import google.generativeai as genai
import os
from dotenv import load_dotenv

def summarize_transcript(transcript_file, output_file="outputs/meeting_summary.txt"):
    """
    Reads a meeting transcript, generates a professional, structured summary using the Gemini API,
    and saves it to a file.
    """
    try:
        text = Path(transcript_file).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: The transcript file was not found at {transcript_file}")
        return

    # Load API key from .env file for better security
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY") # Make sure you have this in your .env file
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file.")
        # Fallback to the hardcoded key if needed, but this is not recommended
        api_key = "YOUR_FALLBACK_API_KEY_HERE" 
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    # --- NEW, MORE PROFESSIONAL PROMPT ---
    prompt = f"""
    **Objective:** Analyze the following meeting transcript and produce a professional, structured summary suitable for executive review.

    **Role:** You are an expert executive assistant. Your task is to distill the conversation into its most critical components with absolute clarity and conciseness.

    **Instructions:**
    1.  Read the entire transcript carefully to understand the context, participants, and flow of conversation.
    2.  Do not include conversational filler, greetings, or off-topic chatter.
    3.  Extract only factual information regarding decisions, commitments, and plans.
    4.  Format the output precisely as specified below, using the provided emojis. Do not add any extra sections or commentary.

    **Transcript to Analyze:**
    ---
    {text}
    ---

    **Required Output Format:**

    📌 **EXECUTIVE SUMMARY**
    A concise, 3-sentence paragraph summarizing the meeting's core purpose, key outcomes, and overall direction. Start with the main topic discussed.

    ✅ **KEY DECISIONS**
    A bulleted list of all concrete decisions that were finalized. Each bullet point should be a clear, unambiguous statement. If no decisions were made, state "No key decisions were finalized in this meeting."
    - [Decision 1]
    - [Decision 2]

    📝 **ACTION ITEMS**
    A checklist of all tasks that were assigned to a specific person. The format must be "Person's Name → Specific Task (Due: Deadline)". If no deadline was mentioned, use "Due: TBD".
    - ☑️ Name → Task (Due: Deadline)
    - ☑️ Name → Task (Due: Deadline)

    ❓ **OPEN QUESTIONS**
    A numbered list of important questions or topics that were raised but not resolved, requiring a follow-up. If all topics were resolved, state "All topics were resolved."
    1. [Unresolved Question 1]
    2. [Unresolved Question 2]
    """

    try:
        response = model.generate_content(prompt)
        result = response.text.strip()

        # Ensure the output directory exists
        Path("outputs").mkdir(exist_ok=True)
        
        Path(output_file).write_text(result, encoding="utf-8")
        print(f"✅ Summary saved to {output_file}")
        print("\n--- Summary Preview ---\n")
        print(result)
    
    except Exception as e:
        print(f"An error occurred while generating the summary: {e}")


if __name__ == "__main__":
    summarize_transcript("outputs/meeting_transcript.txt")

