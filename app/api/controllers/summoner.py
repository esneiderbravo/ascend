from ascend.app import app
from ascend.app.utils.request import get


class SummonerController:
    """
    Summoner Controller.

    Handles summoner controller methods.
    """

    @classmethod
    def get_summoner_info(cls, params):
        """
        Get summoner information.

        Args:
            params (dict): Dictionary containing tagLine and summonerName parameters.

        Returns:
            tuple: Tuple containing a dictionary with summoner response and HTTP status code.
        """
        try:
            tag_line = params.get("tagLine")
            summoner_name = params.get("summonerName")

            # Retrieve API configuration from Flask app
            api_key = app.config.get("RIOT_API_KEY")
            by_riot_id_url_complement = app.config.get("ACCOUNT_BY_RIOT_API_URL")
            americas_api_url = app.config.get("AMERICAS_API_URL")

            # Construct the URL using the configuration values
            url = f"{americas_api_url}{by_riot_id_url_complement}{summoner_name}/{tag_line}/?{api_key}"

            # Get summoner data using the configured URL
            data = get(url)

            return data

        except Exception as e:
            # Handle unexpected errors and return an error response
            print(f"An unexpected error occurred: {e}")
            return {"error": "An unexpected error occurred"}, 500
