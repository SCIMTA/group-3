interface callApiProps {
  API: any;
  payload?: object;
  context?: any;
  onSuccess?: (res: any) => void;
  onError?: (err: any) => void;
  onFinaly?: () => void;
  typeLoading: "isLoading" | "isDialogLoading";
}

export default async function callAPI({
  API,
  context,
  typeLoading = "isLoading",
  payload = null,
  onSuccess,
  onError,
  onFinaly
}: callApiProps) {
  if (context)
    try {
      context.setState({
        [typeLoading]: true
      });
      const res = await API(payload);
      if (onSuccess) onSuccess(res);
      context.setState({
        [typeLoading]: false
      });
    } catch (error) {
      context.setState({
        [typeLoading]: false
      });
      if (onError) onError(error);
    } finally {
      if (onFinaly) onFinaly();
    }
  else
    try {
      const res = await API(payload);
      if (onSuccess) onSuccess(res);
    } catch (error) {
      if (onError) onError(error);
    } finally {
      if (onFinaly) onFinaly();
    }
}

interface callApiHookProps {
  API?: any;
  payload?: object;
  formdata?: object;
  useLoading?: (isLoading: boolean) => void;
  onSuccess?: (res: any) => void;
  onError?: (err: any) => void;
  onFinaly?: () => void;
  typeLoading?: "isLoading" | "isDialogLoading";
}

export async function callAPIHook({
  API,
  payload,
  useLoading,
  onSuccess,
  onError,
  onFinaly,
  formdata
}: callApiHookProps) {
  const data = new FormData();
  try {
    Object.keys(formdata).forEach(key => {
      if (Array.isArray(formdata[key])) {
        formdata[key].forEach(element => {
          data.append(key, element);
        });
      } else data.append(key, formdata[key]);
    });
    // console.log(data);
  } catch (error) {}
  if (payload == null || payload == undefined) payload = data;
  if (useLoading)
    try {
      useLoading(true);
      const res = await API(payload);
      if (onSuccess) onSuccess(res);
      useLoading(false);
    } catch (error) {
      useLoading(false);
      if (onError) onError(error);
    } finally {
      if (onFinaly) onFinaly();
    }
  else
    try {
      const res = await API(payload);
      if (onSuccess) onSuccess(res);
    } catch (error) {
      if (onError) onError(error);
    } finally {
      if (onFinaly) onFinaly();
    }
}
