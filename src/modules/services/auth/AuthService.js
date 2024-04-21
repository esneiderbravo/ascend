import { AUTH_SERVICE_URL } from "../../utils/constants";
import HTTPHandler from "../../utils/httpHandler";

/*
 * Authenticate user
 * @param {String} token
 * @return {Promise}
 * */
export const authenticateUser = async (token) => {
  const body = { token: token };
  return await HTTPHandler.auth(AUTH_SERVICE_URL, body);
};
