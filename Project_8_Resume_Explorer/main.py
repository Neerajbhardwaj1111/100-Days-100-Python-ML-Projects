import PyPDF2  # For reading PDF content
import tkinter as tk  # For GUI interface
from tkinter import filedialog, messagebox, scrolledtext
import re  # For text processing
from collections import Counter  # For keyword analysis


def read_pdf(file_path):
    """Extract text from a PDF file"""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF: {str(e)}")
    return text

def analyze_resume(text):
    """Perform basic analysis on resume text"""
    analysis = {}
    
    # Word count
    words = re.findall(r'\w+', text.lower())
    analysis['word_count'] = len(words)
    
    # Common skills/keywords
    skills = ['python', 'java', 'c++', 'sql', 'machine learning', 
              'data analysis', 'project management', 'communication']
    found_skills = [skill for skill in skills if skill in text.lower()]
    analysis['skills'] = found_skills
    
    # Contact information extraction
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    analysis['emails'] = emails
    
    return analysis

class ResumeViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Viewer")
        
        # Create UI elements
        self.btn_open = tk.Button(root, text="Open PDF", command=self.open_file)
        self.btn_open.pack(pady=10)
        
        self.txt_display = scrolledtext.ScrolledText(root, width=80, height=25)
        self.txt_display.pack(pady=10)
        
        self.lbl_analysis = tk.Label(root, text="Analysis Results:", anchor='w')
        self.lbl_analysis.pack(fill='x', padx=10)
        
        self.txt_analysis = scrolledtext.ScrolledText(root, width=80, height=10)
        self.txt_analysis.pack(pady=10)
    
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            text = read_pdf(file_path)
            self.txt_display.delete(1.0, tk.END)
            self.txt_display.insert(tk.END, text)
            
            analysis = analyze_resume(text)
            self.display_analysis(analysis)
    
    def display_analysis(self, analysis):
        self.txt_analysis.delete(1.0, tk.END)
        
        self.txt_analysis.insert(tk.END, f"Word Count: {analysis['word_count']}\n\n")
        
        self.txt_analysis.insert(tk.END, "Found Skills:\n")
        for skill in analysis['skills']:
            self.txt_analysis.insert(tk.END, f"- {skill.title()}\n")
        
        self.txt_analysis.insert(tk.END, "\nContact Information:\n")
        for email in analysis['emails']:
            self.txt_analysis.insert(tk.END, f"- {email}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResumeViewerApp(root)
    root.mainloop()