pub fn elsup(
    elem_vtx: &[usize],
    num_vtx_par_elem: usize,
    num_vtx: usize) -> (Vec<usize>, Vec<usize>) {
    let num_elem = elem_vtx.len() / num_vtx_par_elem;
    assert_eq!(elem_vtx.len(), num_elem*num_vtx_par_elem);
    let mut elsup_ind = Vec::<usize>::new();
    elsup_ind.resize(num_vtx + 1, 0);
    for ielem in 0..num_elem {
        for inoel in 0..num_vtx_par_elem {
            let ino1 = elem_vtx[ielem * num_vtx_par_elem + inoel];
            let ino1 = ino1 as usize;
            elsup_ind[ino1 + 1] += 1;
        }
    }
    for ivtx in 0..num_vtx {
        elsup_ind[ivtx + 1] += elsup_ind[ivtx];
    }
    let nelsup = elsup_ind[num_vtx];
    let mut elsup = Vec::<usize>::new();
    elsup.resize(nelsup, 0);
    for ielem in 0..num_elem {
        for inode in 0..num_vtx_par_elem {
            let ivtx1 = elem_vtx[ielem * num_vtx_par_elem + inode];
            let ivtx1 = ivtx1 as usize;
            let ielem0 = elsup_ind[ivtx1];
            elsup[ielem0] = ielem;
            elsup_ind[ivtx1] += 1;
        }
    }
    for ivtx in (1..num_vtx).rev() {
        elsup_ind[ivtx] = elsup_ind[ivtx - 1];
    }
    elsup_ind[0] = 0;
    (elsup_ind, elsup)
}

pub fn psup(
    elem_vtx: &[usize],
    elsup_ind: &Vec<usize>,
    elsup: &Vec<usize>,
    num_vtx_par_elem: usize,
    num_vtx: usize) -> (Vec<usize>, Vec<usize>) {
    let mut psup_ind = Vec::<usize>::new();
    let mut aflg = Vec::<usize>::new();
    aflg.resize(num_vtx, usize::MAX);
    psup_ind.resize(num_vtx + 1, Default::default());
    for ipoint in 0..num_vtx {
        aflg[ipoint] = ipoint;
        for ielsup in elsup_ind[ipoint]..elsup_ind[ipoint + 1] {
            let jelem = elsup[ielsup];
            for jnoel in 0..num_vtx_par_elem {
                let jnode = elem_vtx[jelem * num_vtx_par_elem + jnoel];
                if aflg[jnode] != ipoint {
                    aflg[jnode] = ipoint;
                    psup_ind[ipoint + 1] += 1;
                }
            }
        }
    }
    for ipoint in 0..num_vtx {
        psup_ind[ipoint + 1] += psup_ind[ipoint];
    }
    let npsup = psup_ind[num_vtx];
    let mut psup = Vec::<usize>::new();
    psup.resize(npsup, 0);
    for ipoint in 0..num_vtx { aflg[ipoint] = usize::MAX; }
    for ipoint in 0..num_vtx {
        aflg[ipoint] = ipoint;
        for ielsup in elsup_ind[ipoint]..elsup_ind[ipoint + 1] {
            let jelem = elsup[ielsup];
            for jnoel in 0..num_vtx_par_elem {
                let jnode = elem_vtx[jelem * num_vtx_par_elem + jnoel];
                if aflg[jnode] != ipoint {
                    aflg[jnode] = ipoint;
                    let ind = psup_ind[ipoint];
                    psup[ind] = jnode;
                    psup_ind[ipoint] += 1;
                }
            }
        }
    }
    for ipoint in (1..num_vtx).rev() {
        psup_ind[ipoint] = psup_ind[ipoint - 1];
    }
    psup_ind[0] = 0;
    (psup_ind, psup)
}

pub fn psup_elem_edge(
    elem_vtx: &[usize],
    num_node_par_elem: usize,
    edges_par_elem: &[usize],
    elsup_ind: &Vec<usize>,
    elsup: &Vec<usize>,
    is_bidirectional: bool) -> (Vec<usize>, Vec<usize>) {
    let num_edge_par_elem = edges_par_elem.len() / 2;
    assert!(edges_par_elem.len() == num_edge_par_elem * 2);
    let mut psup_ind = Vec::<usize>::new();
    let mut psup = Vec::<usize>::new();

    let nvtx = elsup_ind.len() - 1;
    psup_ind.resize(nvtx + 1, 0);
    psup_ind[0] = 0;
    for ip in 0..nvtx {
        let mut set_vtx_idx = std::collections::BTreeSet::new();
        for ielsup in elsup_ind[ip]..elsup_ind[ip + 1] {
            let ielem0 = elsup[ielsup];
            for iedge in 0..num_edge_par_elem {
                let inode0 = edges_par_elem[iedge * 2 + 0];
                let inode1 = edges_par_elem[iedge * 2 + 1];
                let ip0 = elem_vtx[ielem0 * num_node_par_elem + inode0];
                let ip1 = elem_vtx[ielem0 * num_node_par_elem + inode1];
                if ip0 != ip && ip1 != ip { continue; }
                if ip0 == ip {
                    if is_bidirectional || ip1 > ip {
                        set_vtx_idx.insert(ip1);
                    }
                } else {
                    if is_bidirectional || ip0 > ip {
                        set_vtx_idx.insert(ip0);
                    }
                }
            }
        }
        for itr in &set_vtx_idx {
            psup.push((*itr).try_into().unwrap());
        }
        psup_ind[ip + 1] = psup_ind[ip] + set_vtx_idx.len();
    }
    (psup_ind, psup)
}

/// making vertex indexes list of edges from psup (point surrounding point)
pub fn mshline_psup(
    psup_ind: &Vec<usize>,
    psup: &Vec<usize>) -> Vec::<usize> {
    let mut line_vtx = Vec::<usize>::with_capacity(psup.len() * 2);
    let np = psup_ind.len() - 1;
    for ip in 0..np {
        for ipsup in psup_ind[ip]..psup_ind[ip + 1] {
            let jp = psup[ipsup];
            line_vtx.push(ip);
            line_vtx.push(jp);
        }
    }
    line_vtx
}

pub fn mshline(
    elem_vtx: &[usize],
    num_vtx_par_elem: usize,
    edges_par_elem: &[usize],
    num_vtx: usize) -> Vec::<usize>
{
    let elsup = elsup(
        elem_vtx, num_vtx_par_elem, num_vtx);
    let psup = psup_elem_edge(
        elem_vtx, num_vtx_par_elem,
        edges_par_elem,
        &elsup.0, &elsup.1,
        false);
    mshline_psup(&psup.0, &psup.1)
}

pub fn tri_from_quad(
    quad_vtx: &[usize]) -> Vec<usize>
{
    let nquad = quad_vtx.len() / 4;
    let mut tri_vtx = vec![0; nquad*2*3];
    for iquad in 0..nquad {
        tri_vtx[iquad * 6 + 0] = quad_vtx[iquad * 4 + 0];
        tri_vtx[iquad * 6 + 1] = quad_vtx[iquad * 4 + 1];
        tri_vtx[iquad * 6 + 2] = quad_vtx[iquad * 4 + 2];
        //
        tri_vtx[iquad * 6 + 3] = quad_vtx[iquad * 4 + 0];
        tri_vtx[iquad * 6 + 4] = quad_vtx[iquad * 4 + 2];
        tri_vtx[iquad * 6 + 5] = quad_vtx[iquad * 4 + 3];
    }
    tri_vtx
}