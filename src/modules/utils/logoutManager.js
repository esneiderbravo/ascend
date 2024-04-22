import { setAuthData, setNotification } from "../actions/state";

/**
 * Manager for user logout operations.
 */
class LogoutManager {
  /**
   * Logs out the user by clearing authentication data and session storage.
   * @param {Object} state - Current state object.
   * @param {Function} dispatch - Dispatch function from Redux or React context.
   * @param {Object} language - Language object containing logout messages.
   */
  static logout(state, dispatch, language) {
    // Clear authentication data from state
    const emptyAuthData = {};
    dispatch(setAuthData(emptyAuthData));

    // Clear session and local storage
    sessionStorage.clear();
    localStorage.clear();
    dispatch(
      setNotification({
        type: "success",
        info: language["logoutMessages"]["success"],
      }),
    );
  }
}

export default LogoutManager;
