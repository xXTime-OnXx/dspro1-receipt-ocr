'use client';

import { JSX, useState } from 'react';
import styles from '../page.module.scss';
import Link from 'next/link';
import InsertPhotoIcon from '@mui/icons-material/InsertPhoto';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera';
import { postReceiptImage } from '@/app/requests/receiptItems.request';
import { ReceiptItem } from '@/types/receiptItem.types';
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';

export interface SimpleDialogProps {
  open: boolean;
  selectedItem: ReceiptItem;
  onClose: (value: ReceiptItem) => void;
}

const TwintRequestAndSplitPage: React.FC = (): JSX.Element => {
  const mockUsers: string[] = ['Alice', 'Bob', 'Charlie', 'David'];
  const mockReceiptItems: ReceiptItem[] = [
    { quantity: '1', name: 'Coke', price: 2.5, splittedUsers: [] },
    { quantity: '2', name: 'Fanta', price: 5.0, splittedUsers: [] },
    { quantity: '2', name: 'Ice Cream', price: 10.0, splittedUsers: [] },
  ];
  const [receiptItems, setReceiptItems] = useState<ReceiptItem[] | null>(null);
  const [selectedReceiptItem, setSelectedReceiptItem] =
    useState<ReceiptItem | null>(null);

  const handleReceiptPictureChange = (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    if (event.target.files) {
      postReceiptImage(event.target.files[0])
        .then((res) => {
          setReceiptItems(res.data);
        })
        .catch((e) => {
          console.error(e);
          setReceiptItems(mockReceiptItems);
        });
    }
  };

  const handleSplit = (item: ReceiptItem) => {
    setSelectedReceiptItem(item);
  };

  const getHighestId = () => {
    if (selectedReceiptItem && selectedReceiptItem.splittedUsers.length > 0) {
      return selectedReceiptItem.splittedUsers.reduce((maxId, user) => {
        return user.id > maxId ? user.id : maxId;
      }, selectedReceiptItem.splittedUsers[0].id);
    }
    return -1;
  };

  const handleAddUser = () => {
    console.log('add user');
    if (selectedReceiptItem) {
      const updatedItem = {
        ...selectedReceiptItem,
        splittedUsers: [
          ...selectedReceiptItem.splittedUsers,
          { id: getHighestId() + 1, name: '', price: 0 },
        ],
      };
      setSelectedReceiptItem(updatedItem);
    }
  };

  const handleRemoveUser = (id: number) => {
    console.log('remove user');
    if (selectedReceiptItem) {
      const updatedItem = {
        ...selectedReceiptItem,
        splittedUsers: selectedReceiptItem.splittedUsers.filter(
          (user) => user.id !== id
        ),
      };
      setSelectedReceiptItem(updatedItem);
    }
  };

  const updateSplit = (id: number, name: string, price: number) => {
    if (selectedReceiptItem) {
      const updatedItem = {
        ...selectedReceiptItem,
        splittedUsers: selectedReceiptItem.splittedUsers.map((user) => {
          if (user.id === id) {
            return { id, name, price };
          }
          return user;
        }),
      };
      setSelectedReceiptItem(updatedItem);
    }
  };

  return (
    <>
      <div>RequestAndSplit</div>
      <div className={styles.phoneContainer}>
        <span className={styles.dashboardHeader}>
          <Link className={styles.backButton} href='/demo/twint'>
            {'<'}
          </Link>
          <div className={styles.appTitle}>Request and Split</div>
        </span>
        <div className={styles.tabMenu}>
          <div className={styles.tab}>REQUEST</div>
          <div className={styles.tabActive}>RECEIPT OCR</div>
          <div className={styles.tab}>SPLIT AMOUNT</div>
        </div>
        {!receiptItems && (
          <>
            <div className={styles.transactionsSection}>
              <h3>Select Receipt</h3>
              <span className={styles.inputSection}>
                <label for='LibraryInput'>
                  <InsertPhotoIcon fontSize='large' color='primary' />
                </label>
                <input
                  id='LibraryInput'
                  className={styles.hidden}
                  type='file'
                  accept='.jpg, .jpeg, .png'
                  onChange={handleReceiptPictureChange}
                ></input>
                <div className={styles.divider}></div>
                <label for='CameraInput'>
                  <PhotoCameraIcon fontSize='large' color='primary' />
                </label>
                <input
                  id='CameraInput'
                  className={styles.hidden}
                  type='file'
                  accept='.jpg, .jpeg, .png'
                  onChange={handleReceiptPictureChange}
                ></input>
              </span>
            </div>
            <div className={styles.buttonContainerInactive}>
              <div className={styles.requestMoneyButtonInactive}>
                Request Money
              </div>
            </div>
          </>
        )}

        {receiptItems && (
          <>
            <div className={styles.transactionsSection}>
              <h3>Receipt Items</h3>
              <TableContainer component={Paper}>
                <Table sx={{ maxWidth: 650 }} aria-label='simple table'>
                  <TableHead>
                    <TableRow>
                      <TableCell align='right'>Quantity</TableCell>
                      <TableCell align='right'>Item</TableCell>
                      <TableCell align='right'>Price&nbsp;</TableCell>
                      <TableCell></TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {receiptItems.map((row) => (
                      <TableRow
                        key={row.name}
                        sx={{
                          '&:last-child td, &:last-child th': { border: 0 },
                        }}
                      >
                        <TableCell align='right'>{row.quantity}</TableCell>
                        <TableCell align='right'>{row.name}</TableCell>
                        <TableCell align='right'>
                          {row.price.toFixed(2)}
                        </TableCell>
                        <TableCell align='right'>
                          <button onClick={() => handleSplit(row)}>
                            Split
                          </button>
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </div>
          </>
        )}

        {selectedReceiptItem && (
          <>
            <div className={styles.transactionsSection}>
              <h3>
                Split - {selectedReceiptItem.quantity}{' '}
                {selectedReceiptItem.name}{' '}
                {selectedReceiptItem.price.toFixed(2)}{' '}
              </h3>
              {selectedReceiptItem.splittedUsers.map((user) => (
                <span
                  key={user.id}
                  style={{ display: 'flex', gap: '10px', alignItems: 'center' }}
                >
                  <input
                    type='text'
                    placeholder='Name'
                    value={user.name}
                    onChange={(e) =>
                      updateSplit(
                        user.id,
                        e.target.value.toString(),
                        user.price
                      )
                    }
                    style={{ width: '200px', flex: 1 }}
                  ></input>
                  <input
                    type='number'
                    placeholder='Price'
                    value={user.price}
                    // onChange={(e) => (user.price = parseFloat(e.target.value))}
                    onChange={(e) =>
                      updateSplit(
                        user.id,
                        user.name,
                        parseFloat(e.target.value)
                      )
                    }
                    style={{ width: '20px', flex: 1 }}
                  ></input>
                  <button
                    onClick={() => handleRemoveUser(user.id)}
                    style={{ flex: 1 }}
                  >
                    -
                  </button>
                </span>
              ))}
              <button onClick={handleAddUser}>+</button>
            </div>
          </>
        )}
      </div>

      <div className={styles.buttonContainer}>
        <Link href='/demo/twint'>
          <div className={styles.requestMoneyButton}>Request Money</div>
        </Link>
      </div>
    </>
  );
};

export default TwintRequestAndSplitPage;
