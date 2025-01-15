import axios, { AxiosResponse } from 'axios';

const baseUrl = 'http://localhost:8000';

export const postReceiptImage = async (image: File): Promise<AxiosResponse> => {
  try {
    return await axios.post(baseUrl + '/receipt/image/items', { file: image });
  } catch (e) {
    if (axios.isAxiosError(e)) {
      console.error(e.response?.data);
      throw e.response?.data;
    } else {
      console.error(e);
      throw e;
    }
  }
};
