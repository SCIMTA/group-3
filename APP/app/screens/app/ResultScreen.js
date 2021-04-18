import React, { useState } from "react";
import { connect } from "react-redux";
import ScreenComponent from "@app/components/ScreenComponent";
import { StyleSheet } from "react-native";
import { useEffect } from "react";
import { View } from "react-native";
import { TouchableOpacity } from "react-native";
import WText from "@app/components/WText";
import { colors } from "@app/constants/Theme";
import { FlatList } from "react-native";
import FastImg from "@app/components/FastImage";
import R from "@app/assets/R";
import NavigationUtil from "@app/navigation/NavigationUtil";
import { SCREEN_ROUTER_APP } from "@app/constants/Constant";

const ItemText = ({ title, value }) => {
  return (
    <View
      style={{
        flexDirection: "row",
        justifyContent: "space-between",
        margin: 15
      }}
      children={
        <>
          <WText font="regular18" children={title} />
          <WText color={colors.primary2} font="bold20" children={value} />
        </>
      }
    />
  );
};

const ResultScreen = props => {
  const { answer } = props.navigation.state.params;

  const [trueAnswer, setTrueAnswer] = useState(
    Array.from({ length: 30 }, (v, i) => `x`)
  );
  useEffect(() => {}, []);

  const numToText = n => {
    switch (n) {
      case 1:
        return "A";
      case 2:
        return "B";
      case 3:
        return "C";
      case 4:
        return "D";
    }
  };
  return (
    <ScreenComponent
      leftComponent={
        <TouchableOpacity
          onPress={() => NavigationUtil.navigate(SCREEN_ROUTER_APP.MAIN)}
          children={
            <FastImg
              source={R.images.ic_list}
              tintColor={colors.white}
              style={{ width: 35, aspectRatio: 1 }}
            />
          }
        />
      }
      rightComponent={
        <TouchableOpacity
          onPress={() =>
            NavigationUtil.navigate(SCREEN_ROUTER_APP.ACTION, {
              answer
            })
          }
          children={
            <FastImg
              source={R.images.ic_camera}
              tintColor={colors.white}
              style={{ width: 35, aspectRatio: 1 }}
            />
          }
        />
      }
      titleHeader="Kết quả"
      renderView={
        <>
          <WText
            font="bold18"
            color={colors.primary}
            style={{ marginHorizontal: 10, marginTop: 15 }}
            children="Thông tin"
          />
          <ItemText title="Số báo danh" value="18150015" />
          <ItemText title="Mã đề" value="001" />
          <ItemText title="Điểm" value="7.8" />
          <WText
            font="bold18"
            color={colors.primary}
            style={{ marginHorizontal: 10 }}
            children="Đáp án sai"
          />
          <FlatList
            data={trueAnswer}
            keyExtractor={(e, i) => `${i}`}
            renderItem={({ index, item }) => (
              <View
                style={{ flexDirection: "row", margin: 15 }}
                children={
                  <>
                    <WText
                      style={{ flex: 1, textAlignVertical: "center" }}
                      children={`Câu ${index + 1}:`}
                    />
                    {[1, 2, 3, 4].map(e => (
                      <TouchableOpacity
                        disabled
                        style={{
                          flex: 1,
                          alignItems: "center"
                        }}
                        key={e}
                        children={
                          <WText
                            style={{
                              borderWidth: 1,
                              borderRadius: 60,
                              width: 30,
                              aspectRatio: 1,
                              textAlign: "center",
                              textAlignVertical: "center",
                              color:
                                trueAnswer[index] == numToText(e)
                                  ? colors.white
                                  : "black",
                              backgroundColor:
                                trueAnswer[index] == numToText(e)
                                  ? colors.primary
                                  : "white",
                              borderColor:
                                trueAnswer[index] == numToText(e)
                                  ? colors.primary2
                                  : "black"
                            }}
                            children={numToText(e)}
                          />
                        }
                      />
                    ))}
                  </>
                }
              />
            )}
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
)(ResultScreen);
const styles = StyleSheet.create({});
