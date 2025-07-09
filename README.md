This is a crew of python developer agents. Just enter the requirements of the application and kickoff the crew to get a fully functional application.

Use the below command to pull the docker image and run it.

docker run {environment variables like OpenAI api key} -p 8501:8501 -v {Location where you want to store application directory}:/app/output abhijeethkollarapu/python_devs_crew_app

Make sure to add OpenAI API key as env variable in the above command like -e OPENAI_API_KEY=sk-...
And Pass the absoulte path where you want to store the application directory once created

Once the application is created, change to that directory and run command "uv run app.py" and your application will be accessible on port number 8501

Remember, since the app is direclty dependent on the requirments, try to be clear with the requirements. If you need help with the inputs you neer to provide look at the example below.

Requirements :

    A simple account management system for a trading simulation platform.
    The system should allow users to create an account, deposit funds, and withdraw funds.
    The system should allow users to record that they have bought or sold shares, providing a quantity.
    The system should calculate the total value of the user's portfolio, and the profit or loss from the initial deposit.
    The system should be able to report the holdings of the user at any point in time.
    The system should be able to report the profit or loss of the user at any point in time.
    The system should be able to list the transactions that the user has made over time.
    The system should prevent the user from withdrawing funds that would leave them with a negative balance, or
    from buying more shares than they can afford, or selling shares that they don't have.
    The system has access to a function get_share_price(symbol) which returns the current price of a share, and includes a test implementation that returns fixed prices for AAPL, TSLA, GOOGL.

module_name: accounts.py
class_name: Accounts
