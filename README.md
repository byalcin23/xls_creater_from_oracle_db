# :bar_chart: Oracle Query Export and Email Script

This Python script connects to an Oracle database, executes a SQL query, exports the result to an Excel file, and sends the file via email as an attachment.

## :gear: Features

- :link: Connects to Oracle DB using cx_Oracle
- :page_facing_up: Executes a specified SQL query
- :clipboard: Converts the query result to a Pandas DataFrame
- :floppy_disk: Saves the data as an Excel file
- :email: Sends the file via email using mailx

## :clipboard: Requirements

- Python 3.x
- cx_Oracle
- pandas
- openpyxl
- Oracle client libraries installed and configured
- mailx installed and configured on your system

To install the required Python packages:  
pip install cx_Oracle pandas openpyxl

## :wrench: Configuration

Update the following parts of the script:

- conn_str: Replace with your Oracle DB credentials and connection string  
  Example: username/password@hostname:port/service_name

- sql_query1: Replace with your actual SQL query

- file_path2: Optional second attachment, provide the correct path if used

- Email section: Update sender, subject, body, and recipients accordingly

## :rocket: Usage

Run the script manually:  
python3 oracle_query_export_and_email.py

## :lock: Security Notes

- Do not hardcode sensitive data in the script  
- Use environment variables or a secret manager  
- Make sure mail sending complies with your internal policies

## :bust_in_silhouette: Author

Prepared by Bahadır for automation and reporting use cases.  
You are free to modify and adapt to your environment.
