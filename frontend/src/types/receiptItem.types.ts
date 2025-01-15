export interface ReceiptItem {
  quantity: string;
  name: string;
  price: number;
  splittedUsers: { id: number; name: string; price: number }[];
}
