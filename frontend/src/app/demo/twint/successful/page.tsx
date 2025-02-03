import React from 'react';
import styles from '../page.module.scss';
import Link from 'next/link';

const SuccessPage: React.FC = () => {
  return (
    <div className={styles.centeredContainer}>
      <div
        className={styles.phoneContainer}
        style={{ backgroundColor: '#439d46', border: 'none' }}
      >
        <div className={styles.successContainer}>
          <div className={styles.successMessage}>Request successful</div>
        </div>
        <div className={styles.buttonContainer}>
          <Link href='/demo/twint'>
            <div className={styles.okButton}>Ok</div>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default SuccessPage;
