Objective: To create a calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) based on voice input using speech recognition and text-to-speech feedback

                    +-------------------+
                    |    Microphone     |
                    +--------+----------+
                             |
                             v
                    +-------------------+
                    | Speech Recognizer |
                    | (Speech to Text)  |
                    +--------+----------+
                             |
                    "Add 5 and 7"
                             |
                             v
                    +-------------------+
                    | Command Parser    |
                    | Extracts intent & |
                    | operands          |
                    +--------+----------+
                             |
                             v
                    +-------------------+
                    | Calculator Engine |
                    | Performs: + - × ÷ |
                    +--------+----------+
                             |
                             v
                    +-------------------+
                    | Text-to-Speech    |
                    | (Result as voice) |
                    +--------+----------+
                             |
                             v
                         🔊 Speaker





CONCEPTS USED

Natural Language Processing (NLP) – for command understanding

Speech Recognition – converting voice to text

Parsing algorithms – for interpreting arithmetic commands

Event-driven programming – for handling continuous listening and responding