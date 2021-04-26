import React, { useState } from "react";
import { connect } from "react-redux";
import ScreenComponent from "@app/components/ScreenComponent";
import { StyleSheet } from "react-native";
import { useEffect } from "react";
import { View } from "react-native";
import { TouchableOpacity } from "react-native";
import WText from "@app/components/WText";
import { colors } from "@app/constants/Theme";
import InputText from "@app/components/InputText";
import R from "@app/assets/R";
import { FlatList } from "react-native";
import NavigationUtil from "@app/navigation/NavigationUtil";
import { SCREEN_ROUTER_APP } from "@app/constants/Constant";
import AsyncStorage from "@react-native-community/async-storage";
import reactotron from "@app/reactotron/ReactotronConfig";

const AddScreen = props => {
  const { numQuestion, getData } = props.navigation.state.params;
  const [name, setName] = useState(props.navigation.state.params.title || "");
  const isUpdate = !!props.navigation.state.params.title;
  const callApiAddAnswer = async () => {
    let oldData = JSON.parse(await AsyncStorage.getItem("data"));
    if (isUpdate) {
      const id = props.navigation.state.params.id;
      const indexValue = oldData.findIndex(e => e.id == id);
      oldData[indexValue] = {
        id,
        title: name,
        answer: answer.join("")
      };
    } else
      oldData.push({
        id: new Date().getTime() + "",
        title: name,
        answer: answer.join("")
      });
    reactotron.log(oldData);
    AsyncStorage.setItem("data", JSON.stringify(oldData));
    if (getData) getData();
    NavigationUtil.navigate(SCREEN_ROUTER_APP.MAIN);
  };
  const asw = props.navigation.state.params.answer;
  const [answer, setAnswer] = useState(
    !!asw
      ? [...props.navigation.state.params.answer]
      : Array.from({ length: numQuestion || 30 }, (v, i) => `x`)
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
  const isValid = name.length > 0 && !answer.includes("x");
  return (
    <ScreenComponent
      back
      titleHeader={isUpdate ? "Cập nhật" : "Tạo đề"}
      renderView={
        <>
          <InputText
            value={name}
            onChangeText={setName}
            icon={R.images.ic_paper}
            placeholder="Tên đề thi"
          />
          <FlatList
            data={answer}
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
                        style={{
                          flex: 1,
                          alignItems: "center"
                        }}
                        onPress={() => {
                          answer[index] = numToText(e);
                          setAnswer([...answer]);
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
                                answer[index] == numToText(e)
                                  ? colors.white
                                  : "black",
                              backgroundColor:
                                answer[index] == numToText(e)
                                  ? colors.primary
                                  : "white",
                              borderColor:
                                answer[index] == numToText(e)
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
          <TouchableOpacity
            onPress={callApiAddAnswer}
            style={{
              backgroundColor: isValid ? colors.primary : colors.inactive,
              padding: 15
            }}
            disabled={!isValid}
            children={
              <WText
                style={{
                  textAlign: "center"
                }}
                font="bold16"
                color={colors.white}
                children={(isUpdate ? "Cập nhật" : "Tạo đề").toUpperCase()}
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
)(AddScreen);
const styles = StyleSheet.create({});
