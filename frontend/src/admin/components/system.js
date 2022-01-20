import {useState, useEffect} from 'react'
import {Container, Row, Col} from 'react-bootstrap';
import {Outlet, useNavigate} from 'react-router-dom';
import AdminNavigation from './navigation';

const AdminSystem = () => {
  const [activeTarget, setActiveTarget] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const target = document.getElementsByClassName("default")[0]
    target.click()

  }, [])

  const setActive = (url) => (e) => {
    e.preventDefault()
    if (activeTarget != null) {
      activeTarget.classList.remove("active")
    }
    setActiveTarget(e.target)
    e.target.classList.add("active")
    navigate(url)
  }

  return (
    <Container className="h-100">
      <AdminNavigation system/>
      <Row className="h-100">
        <Col md={3} className="border-end">
          <Row className="m-2">
            <a id="add_post" className="m-2 text-decoration-none text-secondary default" onClick={setActive("gernes")}>Danh sách thể loại</a>
            <a id="add_feed" className="m-2 text-decoration-none text-secondary" onClick={setActive("publishers")}>Danh sách các trang báo</a>
          </Row>
        </Col>
        <Col md={9}>
          <Outlet />
        </Col>
      </Row>
    </Container>
  )
}

export default AdminSystem
