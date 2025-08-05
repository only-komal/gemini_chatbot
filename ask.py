import os
import sys
import google.generativeai as genai
def main():
    try:
        query=" ".join(sys.argv[1:])
        if not query:
            print("Please ask a question")
            return
        api_key=os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("Please set the GEMINI_API_KEY environment variable")
            return
        genai.configure(api_key=api_key)
        model=genai.GenerativeModel("models/gemini-1.5-flash")
        print("processing the query...please wait")
        response=model.generate_content(query)
        print("Response:")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")            
if __name__ == "__main__":
    main() 