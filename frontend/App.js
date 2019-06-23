import React, { Component } from 'react'
import { createStackNavigator, createAppContainer } from 'react-navigation'

import CaptureImage from './src/views/CaptureImage'

const Navigator = createStackNavigator(
  {
    CaptureImage: CaptureImage
  },
  {
    defaultNavigationOptions: ({ navigation }) => ({
      header: null
    })
  }
)

const AppContainer = createAppContainer(Navigator);

export default class App extends Component {
  render() {
    return (
      <AppContainer />
    )
  }
}