import Link from 'next/link';
import styles from '@/app/page.module.css';

export default function Home() {
  return (
    <div className={styles.container}>
      <h1>Receipt OCR</h1>
      <div>
        <Link className={styles.link} href='/demo/api'>
          API Demo
        </Link>
      </div>
      <div>
        <Link className={styles.link} href='/demo/twint'>
          Twint Demo
        </Link>
      </div>
    </div>
  );
}
