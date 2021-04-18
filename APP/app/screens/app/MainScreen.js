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
              let num = parseInt(text.replace(",", "").replace(".", ""));
              if (num > 120) num = "120";
              setNumQuestion(num);
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
              backgroundColor: colors.primary,
              borderRadius: 5,
              margin: 10
            }}
            children={
              <WText
                font="bold16"
                color={colors.white}
                style={{
                  textAlign: "center",
                  padding: 15
                }}
                children="Tạo đề"
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
                style={{
                  backgroundColor: colors.primary2,
                  padding: 15,
                  margin: 15,
                  borderRadius: 5
                }}
                children={
                  <WText
                    font="regular18"
                    color={colors.white}
                    children={item.title}
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
