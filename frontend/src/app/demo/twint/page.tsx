import { JSX } from 'react';
import styles from './page.module.scss';
import Link from 'next/link';

const TwintDemoPage: React.FC = (): JSX.Element => {
  return (
    <>
      <div className={styles.centeredContainer}>
        <div className={styles.phoneContainer}>
          <div className={styles.dashboardHeader}>
            <div className={styles.appTitle}>TWINT</div>
          </div>
          <div className={styles.dashboardBanner}>
            <p>Benefit and save with our Super Deals</p>
          </div>
          <div className={styles.transactionsSection}>
            <h3>Transactions</h3>
            <div className={styles.transaction}>
              <div className={styles.transactionIcon}>🛒</div>
              <div className={styles.transactionDetails}>
                <p>Nordstern</p>
                <span>05 Jan</span>
              </div>
              <div className={styles.transactionAmount}>-69.60</div>
            </div>
            <p className={styles.showAllLink}>Show all</p>
          </div>
          <div className={styles.partnerFunctionsSection}>
            <h3>Partner functions</h3>
            <div className={styles.partnerFunctions}>
              <div className={styles.functionCard}>Super Deals</div>
              <div className={styles.functionCard}>Spin & Win</div>
              <div className={styles.functionCard}>Parking</div>
              <div className={styles.functionCard}>Digital vouchers</div>
            </div>
            <p className={styles.showAllLink}>Show all</p>
          </div>
          <div className={styles.bottomActions}>
            <div className={styles.sendButton}>Send</div>
            <Link
              className={styles.requestButton}
              href='/demo/twint/request-and-split'
            >
              Request and split
            </Link>
          </div>
          <div className={styles.payButton}>Pay</div>
        </div>
      </div>
    </>
  );
};

export default TwintDemoPage;
