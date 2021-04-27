import React, { useState } from "react";
import { connect } from "react-redux";
import ScreenComponent from "@app/components/ScreenComponent";
import { StyleSheet } from "react-native";
import { useEffect } from "react";
import { TouchableOpacity } from "react-native";
import WText from "@app/components/WText";
import { colors } from "@app/constants/Theme";
import NavigationUtil from "@app/navigation/NavigationUtil";
import { SCREEN_ROUTER_APP } from "@app/constants/Constant";
import AsyncStorage from "@react-native-community/async-storage";
import { FlatList } from "react-native";
import InputText from "@app/components/InputText";
import R from "@app/assets/R";
import reactotron from "@app/reactotron/ReactotronConfig";
import { RefreshControl } from "react-native";
import { showOption } from "@app/utils/AlertHelper";
import FastImg from "@app/components/FastImage";

const MainScreen = props => {
  const [data, setData] = useState([]);
  const getData = async () => {
    const data = await AsyncStorage.getItem("data");
    if (!data) AsyncStorage.setItem("data", JSON.stringify([]));
    else setData(JSON.parse(data));
  };
  const [numQuestion, setNumQuestion] = useState("30");
  useEffect(() => {
    getData();
  }, []);
  const deleteItem = async id => {
    let d = await AsyncStorage.getItem("data");
    d = d.filter(e => e.id != id);
    setData(JSON.parse(d));
  };
  return (
    <ScreenComponent
      titleHeader="Chấm điểm trắc nghiệm"
      renderView={
        <>
          <WText
            style={{
              color: colors.primary,
              marginHorizontal: 10,
              marginTop: 10
            }}
            font="bold20"
            children="Tạo đề thi mới"
          />
          <InputText
            value={numQuestion}
            keyboardType="number-pad"
            maxLength={3}
            onChangeText={text => {
              if (text) {
                let num = parseInt(text.replace(",", "").replace(".", ""));
                if (num > 120) num = "120";
                setNumQuestion(num);
              } else setNumQuestion(text);
            }}
            icon={R.images.ic_num_question}
            placeholder="Số câu, ví dụ: 30, tối đa 120 câu"
          />
          <TouchableOpacity
            onPress={() => {
              NavigationUtil.navigate(SCREEN_ROUTER_APP.ADD, {
                numQuestion: parseInt(numQuestion),
                getData
              });
            }}
            style={{
              alignSelf: "center",
              width: "95%",
              margin: 10
            }}
            children={
              <FastImg
                resizeMode="cover"
                style={{
                  borderRadius: 5,
                  shadowColor: "#000",
                  shadowOffset: {
                    width: 0,
                    height: 12
                  },
                  shadowOpacity: 0.58,
                  shadowRadius: 16.0,
                  elevation: 8
                }}
                source={R.images.bg_create_item}
                children={
                  <WText
                    font="bold16"
                    color={"black"}
                    style={{
                      padding: 15,
                      backgroundColor: "rgba(255,255,255,0.7)",
                      alignSelf: "flex-start"
                    }}
                    children="Tạo đề"
                  />
                }
              />
            }
          />
          <WText
            style={{ color: colors.primary, marginHorizontal: 10 }}
            font="bold20"
            children="Danh sách đề thi"
          />
          <FlatList
            data={data}
            refreshControl={
              <RefreshControl refreshing={false} onRefresh={getData} />
            }
            keyExtractor={(item, index) => `${index}`}
            renderItem={({ item, index }) => (
              <TouchableOpacity
                onPress={() => {
                  NavigationUtil.navigate(SCREEN_ROUTER_APP.ACTION, {
                    answer: item.answer
                  });
                }}
                onLongPress={() => {
                  showOption("", "", [
                    {
                      text: "Cập nhật",
                      onPress: () =>
                        NavigationUtil.navigate(SCREEN_ROUTER_APP.ADD, {
                          ...item,
                          getData
                        })
                    },
                    {
                      text: "Xoá",
                      onPress: () => {
                        deleteItem(item.id);
                      }
                    }
                  ]);
                }}
                style={{
                  margin: 15
                }}
                children={
                  <FastImg
                    resizeMode="cover"
                    source={R.images.bg_item}
                    style={{
                      borderRadius: 5,
                      shadowColor: "#000",
                      shadowOffset: {
                        width: 0,
                        height: 12
                      },
                      shadowOpacity: 0.58,
                      shadowRadius: 16.0,
                      elevation: 8
                    }}
                    children={
                      <WText
                        font="regular18"
                        color={colors.white}
                        style={{
                          backgroundColor: "rgba(0,0,0,0.8)",
                          padding: 15,
                          alignSelf: "flex-start"
                        }}
                        children={item.title}
                      />
                    }
                  />
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
)(MainScreen);
const styles = StyleSheet.create({});
