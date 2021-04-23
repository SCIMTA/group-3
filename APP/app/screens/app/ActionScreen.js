import React, { useState } from "react";
import { connect } from "react-redux";
import ScreenComponent from "@app/components/ScreenComponent";
import { StyleSheet } from "react-native";
import { useEffect } from "react";
import { View } from "react-native";
import { TouchableOpacity } from "react-native";
import { colors } from "@app/constants/Theme";
import { RNCamera } from "react-native-camera";
import { useRef } from "react";
import NavigationUtil from "@app/navigation/NavigationUtil";
import { SCREEN_ROUTER_APP } from "@app/constants/Constant";
import reactotron from "reactotron-react-native";
import { callAPIHook } from "@app/utils/CallApiHelper";
import { predict } from "@api";
const ActionScreen = props => {
  const camera = useRef(null);
  const [isLoading, setLoading] = useState(false);
  const { answer } = props.navigation.state.params;
  // reactotron.log(answer);
  useEffect(() => {}, []);
  const callApiPredict = () => {
    camera.current
      .takePictureAsync({
        width: 1600,
        orientation: RNCamera.Constants.Orientation.portrait
      })
      .then(res => {
        callAPIHook({
          API: predict,
          useLoading: setLoading,
          formdata: {
            image: {
              uri: res.uri,
              name: res.uri.split("/").pop(),
              type: "image/jpeg",
              filename: new Date().getTime() + `.jpeg`
            },
            answer
          },
          onSuccess: res => {
            NavigationUtil.navigate(SCREEN_ROUTER_APP.RESULT, {
              answer
            });
          }
        });
      });
  };
  const QR_BOX_SIZE_WIDTH = width * 0.9;
  const QR_BOX_SIZE_HEIGHT = height * 0.7;
  const verticalHeight = (height - QR_BOX_SIZE_HEIGHT) / 4;
  const verticalWidth = width;
  const horizontalHeight = QR_BOX_SIZE_HEIGHT;
  const horizontalWidth = (width - QR_BOX_SIZE_WIDTH) / 2;
  return (
    <ScreenComponent
      dialogLoading={isLoading}
      back
      titleHeader="Chấm điểm"
      renderView={
        <>
          <RNCamera
            // children={
            //   <View style={{ flex: 1 }}>
            //     <View
            //       style={{
            //         width: verticalWidth,
            //         height: verticalHeight,
            //         backgroundColor: "rgba(0,0,0,0.5)"
            //       }}
            //     />

            //     <View
            //       style={{ height: QR_BOX_SIZE_HEIGHT, flexDirection: "row" }}
            //     >
            //       <View
            //         style={{
            //           width: horizontalWidth,
            //           height: horizontalHeight,
            //           backgroundColor: "rgba(0,0,0,0.5)"
            //         }}
            //       />
            //       <View
            //         style={{
            //           width: QR_BOX_SIZE_WIDTH,
            //           height: QR_BOX_SIZE_HEIGHT
            //         }}
            //       />
            //       <View
            //         style={{
            //           width: horizontalWidth,
            //           height: horizontalHeight,
            //           backgroundColor: "rgba(0,0,0,0.5)"
            //         }}
            //       />
            //     </View>
            //     <View
            //       style={{
            //         width: verticalWidth,
            //         height: verticalHeight,
            //         backgroundColor: "rgba(0,0,0,0.5)"
            //       }}
            //     />
            //   </View>
            // }
            ref={camera}
            type="back"
            style={{ flex: 6 }}
          />
          <View
            style={{
              backgroundColor: colors.primary,
              flex: 1
            }}
            children={
              <TouchableOpacity
                onPress={callApiPredict}
                style={{
                  alignSelf: "center",
                  borderRadius: (width / 6) * 2,
                  backgroundColor: colors.white,
                  height: width / 6,
                  aspectRatio: 1,
                  overflow: "hidden",
                  marginTop: "5%",
                  borderWidth: 2,
                  borderColor: colors.primary2
                }}
              />
            }
          />
        </>
      }
    />
  );
};

const mapStateToProps = state => ({});

const mapDispatchToProps = {};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(ActionScreen);
const styles = StyleSheet.create({});
