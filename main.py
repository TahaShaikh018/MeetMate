# main.py - The master script to run the entire MeetMate flow

# IMPORTANT: Import the specific functions from your other scripts
from src.transcribe import transcribe
from src.summarize import summarize_transcript
from src.send_email import send_summary_email

def run_full_process(audio_file_path):
    """Runs the complete transcription, summarization, and email process."""
    print("🚀 [Step 1/3] Starting audio transcription...")
    transcribe(audio_file_path)  # <-- CHANGE 1: This line is now active.
    print("✅ Transcription complete!")

    print("\n🚀 [Step 2/3] Generating meeting summary...")
    # This now summarizes the file created by the transcribe step.
    summarize_transcript('outputs/meeting_transcript.txt')
    print("✅ Summary generated!")

    print("\n🚀 [Step 3/3] Sending summary email...")
    send_summary_email()
    
    print("\n🎉🎉🎉 MeetMate flow finished successfully! 🎉🎉🎉")

if __name__ == '__main__':
    # CHANGE 2: The path now points to your corrected audio filename.
    meeting_audio = 'audio/meeting.mp3' 
    run_full_process(meeting_audio)