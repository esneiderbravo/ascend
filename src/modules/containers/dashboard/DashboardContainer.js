import React, { useState } from 'react'
import DashboardContent from '../../components/dashboard/DashboardContent'

/**
 * DashboardContainer Component
 * Renders the DashboardContent component.
 * Can be extended to include logic for fetching data or handling user interactions.
 * @return React.JSX.Element
 */
const DashboardContainer = () => {
  const [formData, setFormData] = useState({
    summonerName: null,
    tagLine: ''
  })
  const handleSubmit = (event) => {
    event.preventDefault()
    console.log(formData)
  }

  return <DashboardContent formData={formData} setFormData={setFormData} handleSubmit={handleSubmit} />
}

// Define propTypes if the component starts accepting props in the future
DashboardContainer.propTypes = {}

export default DashboardContainer
