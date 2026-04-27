import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';

export default function Home(): ReactNode {
  return (
    <Layout description="Kalyan Ram Chimmili's Portfolio">
      <main style={{maxWidth: '600px', margin: '3rem auto', padding: '0 1rem'}}>
        <div style={{textAlign: 'center', marginBottom: '2.5rem'}}>
          <img
            src="/img/pp.jpg"
            alt="Kalyan Ram Chimmili"
            style={{
              width: 160,
              height: 160,
              borderRadius: '30%',
              objectFit: 'cover',
              display: 'block',
              margin: '0 auto',
            }}
          />
          <h1 style={{margin: '1rem 0 0'}}>Kalyan Ram Chimmili</h1>
        </div>

        <h2>Hello!</h2>

        <p>
          I am a Network Engineer at <strong><a href="https://www.iggroup.com/">IG Group</a></strong>, currently
          building <strong> Network as a Service (NaaS)</strong> platforms. My
          work involves automating global infrastructure and developing
          software-driven network solutions.
        </p>

        <p>
          Contact me at{' '}
          <a href="mailto:kalyanram.chimmili@gmail.com">
            kalyanram.chimmili@gmail.com
          </a>
          .
        </p>

        <h2>Sections</h2>
        <ul>
          <li>
            <Link to="/docs/projects">Projects</Link>
          </li>
          <li>
            <Link to="/docs/leetcode">LeetCode DSA</Link>
          </li>
          <li>
            <Link to="/blog">Journey Blog</Link>
          </li>
        </ul>

        <h2>Links</h2>
        <ul>
          <li>
            <a href="mailto:kalyanram.chimmili@gmail.com">Email</a>
          </li>
          <li>
            <a href="https://github.com/kalyanramchimmilli">GitHub</a>
          </li>
          <li>
            <a href="https://www.linkedin.com/in/kalyanramch/">LinkedIn</a>
          </li>
        </ul>
      </main>
    </Layout>
  );
}
