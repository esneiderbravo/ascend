import english from '../language/en_us.json'

const notification = {
  hidden: true,
  message: '',
  type: ''
}

const localStorageAuthData = JSON.parse(localStorage.getItem('authData')) || null

const authData = localStorageAuthData ? { ...localStorageAuthData } : {}

const language = english

const initialState = { language, notification, authData }

/**
 * Reducer
 * @param {Object} state Reducer state. Ie, {notification: {...}, ...}
 * @param {Object} action Reducer action. Ie, {type: "showNotification", payload: {...}}
 */
const reducer = (state, { type, payload }) => {
  switch (type) {
    case 'setLanguage':
      return { ...state, ...payload }

    case 'setAuthData':
      return { ...state, ...payload }

    case 'setNotification':
      return { ...state, ...payload }

    default:
      throw new Error('No valid action')
  }
}

export { initialState, reducer }
