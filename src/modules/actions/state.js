/**
 * Set states
 */
const setAuthData = (authData) => ({
  type: 'setAuthData',
  payload: {
    authData
  }
})

const setLanguage = (language) => ({
  type: 'setLanguage',
  payload: {
    language
  }
})

const setNotification = (notification) => ({
  type: 'setNotification',
  payload: {
    notification
  }
})

export { setAuthData, setLanguage, setNotification }
