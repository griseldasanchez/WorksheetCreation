from flask import Flask, jsonify, request, send_from_directory, redirect, url_for
import pymysql.cursors

app = Flask(__name__, static_folder='static')

# Create a MySQL connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='ugroup_database',
    cursorclass=pymysql.cursors.DictCursor
)

# PROFESSOR ROUTES
# Define route to serve the index.html file
@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/style.css')
def style():
    return send_from_directory('', 'stylesheets/style.css')

@app.route('/styletest.css')
def styletest():
    return send_from_directory('', 'stylesheets/styletest.css')

@app.route('/ProfessorDashboard.html')
def ProfessorDashboard():
    return send_from_directory('', 'htmls/ProfessorDashboard.html')
@app.route('/styleProfessorDash.css')
def styleProfessorDash():
    return send_from_directory('', 'stylesheets/styleProfessorDash.css')

@app.route('/ProfessorViewCreatedWorksheet.html')
def ProfessorViewCreatedWorksheet():
    return send_from_directory('', 'htmls/ProfessorViewCreatedWorksheet.html')
@app.route('/styleProfessorViewCreatedWorksheet.css')
def styleProfessorViewCreatedWorksheet():
    return send_from_directory('', 'stylesheets/styleProfessorViewCreatedWorksheet.css')

@app.route('/ProfessorCreationWorksheet.html')
def ProfessorCreationWorksheet():
    return send_from_directory('', 'htmls/ProfessorCreationWorksheet.html')
@app.route('/styleProfessorCreationWorksheet.css')
def styleProfessorCreationWorksheet():
    return send_from_directory('', 'stylesheets/styleProfessorCreationWorksheet.css')

@app.route('/ProfessorViewGroupWorksheet.html')
def ProfessorViewGroupWorksheet():
    return send_from_directory('', 'htmls/ProfessorViewGroupWorksheet.html')
@app.route('/styleProfessorViewGroupWorksheet.css')
def styleProfessorViewGroupWorksheet():
    return send_from_directory('', 'stylesheets/styleProfessorViewGroupWorksheet.css')

#STDENT ROUTES
@app.route('/StudentDashboard.html')
def StudentDashboard():
    return send_from_directory('', 'htmls/StudentDashboard.html')
@app.route('/styleStudentDash.css')
def styleStudentDash():
    return send_from_directory('', 'stylesheets/styleStudentDash.css')

@app.route('/StudentAcceptWorksheet.html')
def StudentAcceptWorksheet():
    print('in StudentAcceptWorksheet')
    return send_from_directory('', 'htmls/StudentAcceptWorksheet.html')
@app.route('/styleStudentAcceptWorksheet.css')
def styleStudentAcceptWorksheet():
    print('in StudentAcceptWorksheet')
    return send_from_directory('', 'stylesheets/styleStudentAcceptWorksheet.css')

@app.route('/StudentAddGroupMembers.html')
def StudentAddGroupMembers():
    return send_from_directory('', 'htmls/StudentAddGroupMembers.html')
@app.route('/styleStudentAddGroupMembers.css')
def styleStudentAddGroupMembers():
    return send_from_directory('', 'stylesheets/styleStudentAddGroupMembers.css')

# Images
@app.route('/img.jpg')
def serve_background():
    return send_from_directory('', 'images/img.jpg')

@app.route('/module7.jpg')
def serve_image():
    return send_from_directory('', 'images/module7.jpg')

@app.route('/Module7Answers.png')
def serve_answers():
    return send_from_directory('', 'images/Module7Answers.png')



# server connect test 
@app.route('/test-connection')
def test_connection():
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')  # Simple query to test connection
            print('Connected to database!')
            return jsonify({'message': 'Connection to MySQL database successful!'})
    except Exception as e:
        print('Error testing connection:', e)
        return jsonify({'error': 'Failed to connect to MySQL database'}), 500

# inserting the worksheet name
@app.route('/insert_worksheet_name_data', methods=['POST'])
def insert_worksheet_name_data():
    if request.method == 'POST':
        try:
            # Retrieve data from the form
            worksheet_id = request.form['worksheet_name']
            print('Received worksheet name:', worksheet_id)

            # Insert data into the database
            with connection.cursor() as cursor:
                sql = "INSERT INTO Worksheet (worksheet_name) VALUES (%s)"
                cursor.execute(sql, (worksheet_id,))
                connection.commit()
            
            #return redirect(url_for('ProfessorViewCreatedWorksheet', worksheet_name=worksheet_name))

            return jsonify({'message': 'Data for worksheet name inserted successfully'}), 200
        
        except Exception as e:
            print('Error inserting data:', e)
            return jsonify({'error': 'An error occurred while inserting worksheet name'}), 500
    else:
        return jsonify({'error': 'Invalid request method'}), 400
    
#inserting the question type
@app.route('/insert_question_type_data', methods=['POST'])
def insert_question_type_data():
    if request.method == 'POST':
        try:
            # Retrieve data from the form
            question_type_id  = request.form['type_name']
            print('Received question type :', question_type_id)

            # Insert data into the database
            with connection.cursor() as cursor:
                sql = "INSERT INTO QuestionType (type_name) VALUES (%s)"
                cursor.execute(sql, (question_type_id,))
                connection.commit()
            #return redirect(url_for('ProfessorViewCreatedWorksheet', worksheet_name=worksheet_name))

            return jsonify({'message': 'Data inserted for question type successfully'}), 200
        
        except Exception as e:
            print('Error inserting data:', e)
            return jsonify({'error': 'An error occurred while inserting data for question type'}), 500
    else:
        return jsonify({'error': 'Invalid request method'}), 400

# inserting a question
@app.route('/insert_question_data', methods=['POST'])
def insert_question_data():
    if request.method == 'POST':
        try:
            # Retrieve data from the form
            question_id  = request.form['question_prompt']
            print('Received question type :', question_id)

            # Insert data into the database
            with connection.cursor() as cursor:
                sql = "INSERT INTO Question (question_prompt) VALUES (%s)"
                cursor.execute(sql, (question_id,))
                connection.commit()
            
            #return redirect(url_for('ProfessorViewCreatedWorksheet', worksheet_name=worksheet_name))

            return jsonify({'message': 'Data inserted for question type successfully'}), 200
        
        except Exception as e:
            print('Error inserting data:', e)
            return jsonify({'error': 'An error occurred while inserting data for question type'}), 500
    else:
        return jsonify({'error': 'Invalid request method'}), 400

    
# answer option route 
@app.route('/insert_option_data', methods=['POST'])
def insert_option_data():
    if request.method == 'POST':
        try:
            # Retrieve data from the form
            option_a = request.form['option_a']
            option_b = request.form['option_b']
            option_c = request.form['option_c']
            option_d = request.form['option_d']

            # Insert data into the database
            with connection.cursor() as cursor:
                sql = "INSERT INTO Question (option_a, option_b, option_c, option_d) VALUES (%s)"
                cursor.execute(sql, (option_a, option_b, option_c, option_d))
                connection.commit()

            return jsonify({'message': 'Data inserted for answer option successfully'}), 200
        
        except Exception as e:
            print('Error inserting data:', e)
            return jsonify({'error': 'An error occurred while inserting data for option'}), 500
    else:
        return jsonify({'error': 'Invalid request method'}), 400


# answer route
@app.route('/insert_correctanswer_data', methods=['POST'])
def insert_correctanswer_data():
    if request.method == 'POST':
        try:
            # Retrieve data from the form
            correct_answer = request.form['correct_answer']
            print('Received answer :', correct_answer)

            # Insert data into the database
            with connection.cursor() as cursor:
                sql = "INSERT INTO answer (correct_answer) VALUES (%s)"
                cursor.execute(sql, (correct_answer,))
                connection.commit()
            
            return jsonify({'message': 'Data inserted for answer successfully'}), 200
        
        except Exception as e:
            print('Error inserting data:', e)
            return jsonify({'error': 'An error occurred while inserting data for answer'}), 500
    else:
        return jsonify({'error': 'Invalid request method'}), 400



# route to handle requests to the /data endpoint
@app.route('/data')
def get_data():
    try:
        with connection.cursor() as cursor:
            # Query to fetch data from the Questions and Worksheets tables
            query = '''SELECT Question.*, Worksheet.worksheet_name, QuestionType.type_name, Question.question_prompt, Question.option_a, 
            Question.option_b, Question.option_c, Question.option_d, Question.correct_answer FROM Question 
            INNER JOIN Worksheet ON Question.worksheet_id = Worksheet.worksheet_id 
            INNER JOIN QuestionType ON Question.question_type_id = QuestionType.question_type_id'''

            cursor.execute(query)
            results = cursor.fetchall()
            return jsonify(results)
    except Exception as e:
        print('Error executing MySQL query:', e)
        return jsonify({'error': 'An error occurred while fetching data'}), 500

# worksheet data route
@app.route('/create-worksheet', methods=['POST'])
def create_worksheet():
    try:
        # Retrieve the worksheet data from the request
        worksheet_title = request.form.get('worksheetTitle')
        questions = request.form.get('questions').split(',')
        option_a = request.form.get('option_a').split(',')
        option_b = request.form.get('option_b').split(',')
        option_c = request.form.get('option_c').split(',')
        option_d = request.form.get('option_d').split(',')
        answers = request.form.get('answers').split(',')
        question_types = request.form.get('questionTypes').split(',')

        # Print the received data on the server side
        print("Worksheet Title:", worksheet_title)
        print("Questions:", questions)
        print("Option A:", option_a)
        print("Option B:", option_b)
        print("Option C:", option_c)
        print("Option D:", option_d)
        print("Answers:", answers)
        print("Question Types:", question_types)

        # Insert worksheet data into the database
        with connection.cursor() as cursor:
            # Insert the worksheet title into the Worksheet table
            worksheet_query = "INSERT INTO Worksheet (worksheet_name) VALUES (%s)"
            cursor.execute(worksheet_query, (worksheet_title,))
            worksheet_id = cursor.lastrowid
            
            # Loop through the questions and insert them into the Question table
            for i in range(len(questions)):


                question_text = questions[i]
                question_type = question_types[i]
                option_a_text = option_a[i]
                option_b_text = option_b[i]
                option_c_text = option_c[i]
                option_d_text = option_d[i]
                answer_text = answers[i]
                

                # Lookup question type ID based on type name
                question_type_query = "SELECT question_type_id FROM QuestionType WHERE type_name = %s"
                cursor.execute(question_type_query, (question_type,))
                result = cursor.fetchone()

                if result:
                    question_type_id = result['question_type_id']

                    # Insert question into the Question table
                    question_query = '''INSERT INTO Question (worksheet_id, question_prompt, option_a, option_b, 
                    option_c, option_d, correct_answer, question_type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
                    cursor.execute(question_query, (worksheet_id, question_text, option_a_text, option_b_text, option_c_text, option_d_text, answer_text, question_type_id))
                else:
                    print("Question type '{}' not found in the database".format(question_type))
            
            connection.commit()
            return jsonify({"message": "Worksheet created successfully"})
        
    except Exception as e:
        print("Error:", e)
        return "An error occurred while creating the worksheet", 500

@app.route('/view-worksheets')
def view_worksheets():
    return send_from_directory('', 'ProfessorViewCreatedWorksheet.html')

@app.route('/logout')
def logout():
    # Perform logout operations here if needed
    return redirect(url_for('index'))  # Redirect to the home page (index.html)

@app.route('/submit-group')
def submit_group():
    return redirect(url_for('StudentDashboard'))

@app.route('/group1module7', methods=['get'])
def group1module7():
    print('in Group1Module7.html')
    return send_from_directory('','htmls/Group1Module7.html') 

# Start the server
if __name__ == '__main__':
    app.run(debug=True, port=4000)


