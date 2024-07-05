import React, { useContext } from 'react'
import { Box, Button, FormControl, Grid, InputLabel, MenuItem, Select, TextField } from '@mui/material'
import AppContext from '../../context/app'
import logoutManager from '../../utils/logoutManager'
import PropTypes from 'prop-types'

/**
 * DashboardContent Component
 * @return {React.JSX.Element}
 */
const DashboardContent = (props) => {
  const { formData, setFormData, handleSubmit } = props
  const [state, dispatch] = useContext(AppContext)
  const { language } = state

  const handleLogout = () => {
    logoutManager.logout(state, dispatch, language)
  }

  const handleChangesSummonerName = (event) => {
    const summonerName = event.target.value
    setFormData({ ...formData, summonerName: summonerName })
  }

  const handleChangesTagLine = (event) => {
    const tagLine = event.target.value
    setFormData({ ...formData, tagLine: tagLine })
  }

  return (
    <Box container display='flex' flexDirection='column' alignItems='center'>
      <Grid container justifyContent='center' md={12}>
        <h1>Dashboard</h1>
      </Grid>
      <Grid container justifyContent='center' md={12}>
        <Button onClick={handleLogout} variant='contained' color='error'>
          {language['logoutTitleButton']}
        </Button>
      </Grid>
      <Grid container display='flex' justifyContent='center' md={12} mt={10}>
        <form onSubmit={handleSubmit}>
          <Grid container md={12}>
            <Grid item md={6}>
              <FormControl required>
                <TextField
                  label='Summoner Name'
                  name='summonerName'
                  value={formData.summonerName}
                  onChange={handleChangesSummonerName}
                  variant='outlined'
                />
              </FormControl>
            </Grid>
            <Grid item md={4}>
              <FormControl required>
                <InputLabel id='demo-simple-select-label'>Select a region</InputLabel>
                <Select value={formData.tagLine} onChange={handleChangesTagLine} label='Select a region *' required>
                  <MenuItem value={'LAN'}>LAN</MenuItem>
                  <MenuItem value={'LAS'}>LAS</MenuItem>
                  <MenuItem value={'NA'}>NA</MenuItem>
                </Select>
              </FormControl>
            </Grid>
            <Grid item md={2}>
              <Button type='submit' variant='contained' color='primary'>
                Submit
              </Button>
            </Grid>
          </Grid>
        </form>
      </Grid>
    </Box>
  )
}

DashboardContent.propTypes = {
  formData: PropTypes.object,
  setFormData: PropTypes.func,
  handleSubmit: PropTypes.func
}

export default DashboardContent
