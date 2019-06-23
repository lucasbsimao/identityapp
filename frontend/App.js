import React, { Component } from "react";
import { StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { Icon } from 'native-base'

import { RNCamera } from "react-native-camera";

export default class App extends Component {
  takePicture = async () => {
    if (this.camera) {
      const options = { quality: 0.5, base64: true };
      const data = await this.camera.takePictureAsync(options);

      alert(data.uri);
    }
  };

  render() {
    return (
      <View style={styles.container}>
        <RNCamera
          ref={camera => {
            this.camera = camera;
          }}
          style={styles.preview}
          type={RNCamera.Constants.Type.back}
          autoFocus={RNCamera.Constants.AutoFocus.on}
          flashMode={RNCamera.Constants.FlashMode.off}
          captureAudio={false}
          androidCameraPermissionOptions={{
              title: 'Permissão para usar a câmera',
              message: 'Por favor, habilite o uso da câmera para prosseguir',
              buttonPositive: 'Ok',
              buttonNegative: 'Cancelar',
          }}  
        >
          <View style={styles.buttonContainer}>
            <TouchableOpacity onPress={this.takePicture} style={styles.capture}>
              <Icon name="camera" />
            </TouchableOpacity>
          </View>
        </RNCamera>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column",
    backgroundColor: "black"
  },
  preview: {
    flex: 1,
    justifyContent: "flex-end",
    alignItems: "center"
  },
  buttonContainer: {
    flex: 0,
    flexDirection: "row",
    justifyContent: "center"
  },
  capture: {
    backgroundColor: "#eee",
    width: 64,
    height: 64,
    borderWidth: 4,
    borderColor: '#555',
    borderRadius: 100,
    margin: 20,
    marginBottom: 60,
    justifyContent: "center",
    alignItems: "center"
  },
  buttonText: {
    fontSize: 14
  }
});