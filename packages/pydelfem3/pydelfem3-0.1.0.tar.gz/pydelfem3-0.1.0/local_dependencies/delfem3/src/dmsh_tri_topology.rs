#[derive(Clone)]
pub struct DynamicTriangle {
    pub v: [usize; 3],
    pub s: [usize; 3],
}

#[derive(Clone)]
pub struct DynamicVertex {
    pub e: usize,
    pub d: usize,
}


pub fn find_adjacent_edge_index(
    t0: &DynamicTriangle,
    ied0: usize,
    tri_vtx: &Vec::<DynamicTriangle>) -> usize {
    let iv0 = t0.v[(ied0 + 1) % 3];
    let iv1 = t0.v[(ied0 + 2) % 3];
    assert!(iv0 != iv1);
    let it1 = t0.s[ied0];
    assert!(it1 != std::usize::MAX);
    if tri_vtx[it1].v[1] == iv1 && tri_vtx[it1].v[2] == iv0 { return 0; }
    if tri_vtx[it1].v[2] == iv1 && tri_vtx[it1].v[0] == iv0 { return 1; }
    if tri_vtx[it1].v[0] == iv1 && tri_vtx[it1].v[1] == iv0 { return 2; }
    panic!();
}


pub fn assert_dynamic_triangles(
    tri_vtx: &Vec<DynamicTriangle>) {
    let ntri = tri_vtx.len();
    for itri in 0..ntri {
        let tri = &tri_vtx[itri];
        if tri.v[0] == std::usize::MAX {
            assert_eq!(tri.v[1], std::usize::MAX);
            assert_eq!(tri.v[2], std::usize::MAX);
            continue;
        }
        assert!(tri.v[0] != tri.v[1]);
        assert!(tri.v[1] != tri.v[2]);
        assert!(tri.v[2] != tri.v[0]);
        assert!((tri.s[0] != tri.s[1]) || tri.s[0] == std::usize::MAX);
        assert!((tri.s[1] != tri.s[2]) || tri.s[1] == std::usize::MAX);
        assert!((tri.s[2] != tri.s[0]) || tri.s[0] == std::usize::MAX);
        for iedtri in 0..3 {
            if tri.s[iedtri] == std::usize::MAX {
                continue;
            }
            assert!(tri.s[iedtri] < tri_vtx.len());
            let jtri = tri.s[iedtri];
            assert!(jtri < ntri);
            let jno = find_adjacent_edge_index(&tri_vtx[itri], iedtri, &tri_vtx);
            assert_eq!(tri_vtx[jtri].s[jno], itri);
            assert_eq!(tri_vtx[itri].v[(iedtri + 1) % 3], tri_vtx[jtri].v[(jno + 2) % 3]);
            assert_eq!(tri_vtx[itri].v[(iedtri + 2) % 3], tri_vtx[jtri].v[(jno + 1) % 3]);
        }
    }
}

pub fn assert_dynamic_triangle_mesh(
    vtx_tri: &Vec<DynamicVertex>,
    tri_vtx: &Vec<DynamicTriangle>)
{
    let npo = vtx_tri.len();
    let ntri = tri_vtx.len();
    for itri in 0..ntri {
        assert!(tri_vtx[itri].v[0] < npo);
        assert!(tri_vtx[itri].v[0] < npo);
        assert!(tri_vtx[itri].v[0] < npo);
    }
    for ipoin in 0..npo {
        let itri0 = vtx_tri[ipoin].e;
        let inoel0 = vtx_tri[ipoin].d;
        if itri0 != std::usize::MAX {
            assert!(itri0 < tri_vtx.len() && inoel0 < 3 && tri_vtx[itri0].v[inoel0] == ipoin);
        }
    }
}


pub fn flip_edge(
    itri_a: usize,
    ied0: usize,
    vtx_tri: &mut Vec<DynamicVertex>,
    tri_vtx: &mut Vec<DynamicTriangle>) -> bool {
    assert!(itri_a < tri_vtx.len() && ied0 < 3);
    if tri_vtx[itri_a].s[ied0] == std::usize::MAX { return false; }

    let itri_b = tri_vtx[itri_a].s[ied0];
    assert!(itri_b < tri_vtx.len());
    let ied1 = find_adjacent_edge_index(&tri_vtx[itri_a], ied0, tri_vtx);
    assert!(ied1 < 3);
    assert_eq!(tri_vtx[itri_b].s[ied1], itri_a);

    let old_a = tri_vtx[itri_a].clone();
    let old_b = tri_vtx[itri_b].clone();

    let no_a0 = ied0;
    let no_a1 = (ied0 + 1) % 3;
    let no_a2 = (ied0 + 2) % 3;

    let no_b0 = ied1;
    let no_b1 = (ied1 + 1) % 3;
    let no_b2 = (ied1 + 2) % 3;

    assert_eq!(old_a.v[no_a1], old_b.v[no_b2]);
    assert_eq!(old_a.v[no_a2], old_b.v[no_b1]);

    vtx_tri[old_a.v[no_a1]].e = itri_a;
    vtx_tri[old_a.v[no_a1]].d = 0;
    vtx_tri[old_a.v[no_a0]].e = itri_a;
    vtx_tri[old_a.v[no_a0]].d = 2;
    vtx_tri[old_b.v[no_b1]].e = itri_b;
    vtx_tri[old_b.v[no_b1]].d = 0;
    vtx_tri[old_b.v[no_b0]].e = itri_b;
    vtx_tri[old_b.v[no_b0]].d = 2;

    tri_vtx[itri_a].v = [old_a.v[no_a1], old_b.v[no_b0], old_a.v[no_a0]];
    tri_vtx[itri_a].s = [itri_b, old_a.s[no_a2], old_b.s[no_b1]];
    if old_a.s[no_a2] != std::usize::MAX {
        let jt0 = old_a.s[no_a2];
        assert!(jt0 < tri_vtx.len() && jt0 != itri_b && jt0 != itri_a);
        let jno0 = find_adjacent_edge_index(&old_a, no_a2, &tri_vtx);
        tri_vtx[jt0].s[jno0] = itri_a;
    }
    if old_b.s[no_b1] != std::usize::MAX {
        let jt0 = old_b.s[no_b1];
        assert!(jt0 < tri_vtx.len() && jt0 != itri_b && jt0 != itri_a);
        let jno0 = find_adjacent_edge_index(&old_b, no_b1, &tri_vtx);
        tri_vtx[jt0].s[jno0] = itri_a;
    }

    tri_vtx[itri_b].v = [old_b.v[no_b1], old_a.v[no_a0], old_b.v[no_b0]];
    tri_vtx[itri_b].s = [itri_a, old_b.s[no_b2], old_a.s[no_a1]];
    if old_b.s[no_b2] != std::usize::MAX {
        let jt0 = old_b.s[no_b2];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old_b, no_b2, &tri_vtx);
        tri_vtx[jt0].s[jno0] = itri_b;
    }
    if old_a.s[no_a1] != std::usize::MAX {
        let jt0 = old_a.s[no_a1];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old_a, no_a1, &tri_vtx);
        tri_vtx[jt0].s[jno0] = itri_b;
    }
    return true;
}

pub fn move_ccw(
    itri_cur: &mut usize,
    inotri_cur: &mut usize,
    itri_adj: usize,
    tri_vtx: &Vec<DynamicTriangle>) -> bool {
    let inotri1 = (*inotri_cur + 1) % 3;
    if tri_vtx[*itri_cur].s[inotri1] == itri_adj { return false; }
    let itri_nex = tri_vtx[*itri_cur].s[inotri1];
    assert!(itri_nex < tri_vtx.len());
    let ino2 = find_adjacent_edge_index(&tri_vtx[*itri_cur], inotri1, tri_vtx);
    let inotri_nex = (ino2 + 1) % 3;
    assert_eq!(tri_vtx[*itri_cur].v[*inotri_cur], tri_vtx[itri_nex].v[inotri_nex]);
    *itri_cur = itri_nex;
    *inotri_cur = inotri_nex;
    return true;
}

pub fn move_cw(
    itri_cur: &mut usize,
    inotri_cur: &mut usize,
    itri_adj: usize,
    tri_vtx: &Vec<DynamicTriangle>) -> bool {
    let inotri1 = (*inotri_cur + 2) % 3;
    if tri_vtx[*itri_cur].s[inotri1] == itri_adj { return false; }
    let itri_nex = tri_vtx[*itri_cur].s[inotri1];
    assert!(itri_nex < tri_vtx.len());
    let ino2 = find_adjacent_edge_index(&tri_vtx[*itri_cur], inotri1, &tri_vtx);
    let inotri_nex = (ino2 + 2) % 3;
    assert_eq!(tri_vtx[*itri_cur].v[*inotri_cur], tri_vtx[itri_nex].v[inotri_nex]);
    *itri_cur = itri_nex;
    *inotri_cur = inotri_nex;
    return true;
}

pub fn insert_a_point_inside_an_element(
    ipo_ins: usize,
    itri_ins: usize,
    vtx_tri: &mut Vec::<DynamicVertex>,
    tri_vtx: &mut Vec::<DynamicTriangle>) -> bool
{
    assert!(itri_ins < tri_vtx.len());
    assert!(ipo_ins < vtx_tri.len());

    let it_a = itri_ins;
    let it_b = tri_vtx.len();
    let it_c = tri_vtx.len() + 1;

    tri_vtx.resize(tri_vtx.len() + 2, DynamicTriangle { v: [0; 3], s: [0; 3] });
    let old = tri_vtx[itri_ins].clone();

    vtx_tri[ipo_ins].e = it_a;
    vtx_tri[ipo_ins].d = 0;
    vtx_tri[old.v[0]].e = it_b;
    vtx_tri[old.v[0]].d = 2;
    vtx_tri[old.v[1]].e = it_c;
    vtx_tri[old.v[1]].d = 2;
    vtx_tri[old.v[2]].e = it_a;
    vtx_tri[old.v[2]].d = 2;

    tri_vtx[it_a].v = [ipo_ins, old.v[1], old.v[2] ];
    tri_vtx[it_a].s = [old.s[0], it_b, it_c];
    if old.s[0] != std::usize::MAX {
        let jt0 = old.s[0];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old, 0, &tri_vtx);
        tri_vtx[jt0].s[jno0] = it_a;
    }

    tri_vtx[it_b].v = [ipo_ins, old.v[2], old.v[0]];
    tri_vtx[it_b].s = [old.s[1], it_c, it_a];
    if old.s[1] != std::usize::MAX {
        let jt0 = old.s[1];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old, 1, &tri_vtx);
        tri_vtx[jt0].s[jno0] = it_b;
    }

    tri_vtx[it_c].v = [ipo_ins, old.v[0], old.v[1]];
    tri_vtx[it_c].s = [old.s[2], it_a, it_b];
    if old.s[2] != std::usize::MAX {
        let jt0 = old.s[2];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old, 2, &tri_vtx);
        tri_vtx[jt0].s[jno0] = it_c;
    }
    return true;
}

pub fn insert_point_on_elem_edge(
    ipo_ins: usize,
    itri_ins: usize,
    ied_ins: usize,
    vtx_tri: &mut Vec<DynamicVertex>,
    tri_vtx: &mut Vec<DynamicTriangle>) -> bool
{
    assert!(itri_ins < tri_vtx.len());
    assert!(ipo_ins < vtx_tri.len());
    assert!(tri_vtx[itri_ins].s[ied_ins] != std::usize::MAX);

    let itri_adj = tri_vtx[itri_ins].s[ied_ins];
    let ied_adj = find_adjacent_edge_index(&tri_vtx[itri_ins], ied_ins, tri_vtx);
    assert!(itri_adj < tri_vtx.len() && ied_ins < 3);

    let itri0 = itri_ins;
    let itri1 = itri_adj;
    let itri2 = tri_vtx.len();
    let itri3 = tri_vtx.len() + 1;

    tri_vtx.resize(tri_vtx.len() + 2, DynamicTriangle { v: [0; 3], s: [0; 3] });

    let old_a = tri_vtx[itri_ins].clone();
    let old_b = tri_vtx[itri_adj].clone();

    let ino_a0 = ied_ins;
    let ino_a1 = (ied_ins + 1) % 3;
    let ino_a2 = (ied_ins + 2) % 3;

    let ino_b0 = ied_adj;
    let ino_b1 = (ied_adj + 1) % 3;
    let ino_b2 = (ied_adj + 2) % 3;

    assert_eq!(old_a.v[ino_a1], old_b.v[ino_b2]);
    assert_eq!(old_a.v[ino_a2], old_b.v[ino_b1]);
    assert_eq!(old_a.s[ino_a0], itri1);
    assert_eq!(old_b.s[ino_b0], itri0);

    vtx_tri[ipo_ins].e = itri0;
    vtx_tri[ipo_ins].d = 0;
    vtx_tri[old_a.v[ino_a2]].e = itri0;
    vtx_tri[old_a.v[ino_a2]].d = 1;
    vtx_tri[old_a.v[ino_a0]].e = itri1;
    vtx_tri[old_a.v[ino_a0]].d = 1;
    vtx_tri[old_b.v[ino_b2]].e = itri2;
    vtx_tri[old_b.v[ino_b2]].d = 1;
    vtx_tri[old_b.v[ino_b0]].e = itri3;
    vtx_tri[old_b.v[ino_b0]].d = 1;

    tri_vtx[itri0].v = [ipo_ins, old_a.v[ino_a2], old_a.v[ino_a0]];
    tri_vtx[itri0].s = [old_a.s[ino_a1], itri1, itri3];
    if old_a.s[ino_a1] != std::usize::MAX {
        let jt0 = old_a.s[ino_a1];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old_a, ino_a1, tri_vtx);
        tri_vtx[jt0].s[jno0] = itri0;
    }

    tri_vtx[itri1].v = [ipo_ins, old_a.v[ino_a0], old_a.v[ino_a1]];
    tri_vtx[itri1].s = [old_a.s[ino_a2], itri2, itri0];
    if old_a.s[ino_a2] != std::usize::MAX {
        let jt0 = old_a.s[ino_a2];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old_a, ino_a2, tri_vtx);
        tri_vtx[jt0].s[jno0] = itri1;
    }

    tri_vtx[itri2].v = [ipo_ins, old_b.v[ino_b2], old_b.v[ino_b0]];
    tri_vtx[itri2].s = [old_b.s[ino_b1], itri3, itri1];
    if old_b.s[ino_b1] != std::usize::MAX {
        let jt0 = old_b.s[ino_b1];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old_b, ino_b1, tri_vtx);
        tri_vtx[jt0].s[jno0] = itri2;
    }

    tri_vtx[itri3].v = [ipo_ins, old_b.v[ino_b0], old_b.v[ino_b1]];
    tri_vtx[itri3].s = [old_b.s[ino_b2], itri0, itri2];
    if old_b.s[ino_b2] != std::usize::MAX {
        let jt0 = old_b.s[ino_b2];
        assert!(jt0 < tri_vtx.len());
        let jno0 = find_adjacent_edge_index(&old_b, ino_b2, tri_vtx);
        tri_vtx[jt0].s[jno0] = itri3;
    }
    return true;
}


pub fn find_edge_by_looking_around_point(
    itri0: &mut usize,
    inotri0: &mut usize,
    inotri1: &mut usize,
    ipo0: usize,
    ipo1: usize,
    vtx_tri: &Vec<DynamicVertex>,
    tri_vtx: &Vec<DynamicTriangle>) -> bool
{
    let mut itc = vtx_tri[ipo0].e;
    let mut inc = vtx_tri[ipo0].d;
    loop {  // serch clock-wise
        assert_eq!(tri_vtx[itc].v[inc], ipo0);
        let inotri2 = (inc + 1) % 3;
        if tri_vtx[itc].v[inotri2] == ipo1 {
            *itri0 = itc;
            *inotri0 = inc;
            *inotri1 = inotri2;
            assert_eq!(tri_vtx[*itri0].v[*inotri0], ipo0);
            assert_eq!(tri_vtx[*itri0].v[*inotri1], ipo1);
            return true;
        }
        if !move_cw(&mut itc, &mut inc, std::usize::MAX, tri_vtx) {
            break;
        }
        if itc == vtx_tri[ipo0].e {
            return false;
        }
    }
    // -------------
    inc = vtx_tri[ipo0].d;
    itc = vtx_tri[ipo0].e;
    loop { // search counter clock-wise
        assert_eq!(tri_vtx[itc].v[inc], ipo0);
        if !move_ccw(&mut itc, &mut inc, std::usize::MAX, tri_vtx) {
            break;
        }
        if itc == vtx_tri[ipo0].e {  // end if it goes around
            *itri0 = 0;
            *inotri0 = 0;
            *inotri1 = 0;
            return false;
        }
        let inotri2 = (inc + 1) % 3;
        if tri_vtx[itc].v[inotri2] == ipo1 {
            *itri0 = itc;
            *inotri0 = inc;
            *inotri1 = inotri2;
            assert_eq!(tri_vtx[*itri0].v[*inotri0], ipo0);
            assert_eq!(tri_vtx[*itri0].v[*inotri1], ipo1);
            return true;
        }
    }
    return false;
}

pub fn find_edge_by_looking_all_triangles(
    itri0: &mut usize,
    iedtri0: &mut usize,
    ipo0: usize,
    ipo1: usize,
    tri_vtx: &Vec<DynamicTriangle>)
{
    for itri in 0..tri_vtx.len() {
        for iedtri in 0..3 {
            let jpo0 = tri_vtx[itri].v[(iedtri + 0) % 3];
            let jpo1 = tri_vtx[itri].v[(iedtri + 1) % 3];
            if jpo0 == ipo0 && jpo1 == ipo1 {
                *itri0 = itri;
                *iedtri0 = iedtri;
                return;
            }
        }
    }
}

pub fn flag_connected(
    inout_flg: &mut Vec<i32>,
    tri_vtx: &Vec<DynamicTriangle>,
    itri0_ker: usize,
    iflag: i32) {
    assert_eq!(inout_flg.len(), tri_vtx.len());
    assert!(itri0_ker < inout_flg.len());
    inout_flg[itri0_ker] = iflag;
    let mut ind_stack = Vec::<usize>::new();
    ind_stack.push(itri0_ker);
    loop {
        if ind_stack.is_empty() {
            break;
        }
        let itri_cur = ind_stack.pop().unwrap();
        for jtri0 in tri_vtx[itri_cur].s {
            if jtri0 == std::usize::MAX {
                continue;
            }
            if inout_flg[jtri0] != iflag {
                inout_flg[jtri0] = iflag;
                ind_stack.push(jtri0);
            }
        }
    }
}

pub fn delete_tri_flag(
    tri_vtx: &mut Vec<DynamicTriangle>,
    vtx_flag: &mut Vec<i32>,
    flag: i32)
{
    assert_eq!(vtx_flag.len(), tri_vtx.len());
    let ntri0 = tri_vtx.len();
    let mut map01 = vec!(std::usize::MAX; ntri0);
    let mut ntri1 = 0;
    for itri in 0..ntri0 {
        if vtx_flag[itri] != flag {
            map01[itri] = ntri1;
            ntri1 += 1;
        }
    }
    let tri_vtx0 = tri_vtx.clone();
    let vtx_flag0 = vtx_flag.clone();
    tri_vtx.clear();
    tri_vtx.resize(ntri1, DynamicTriangle { v: [0; 3], s: [0; 3] });
    vtx_flag.resize(ntri1, -1);
    for itri0 in 0..tri_vtx0.len() {
        if map01[itri0] != std::usize::MAX {
            let itri1 = map01[itri0];
            assert!(itri1 < ntri1);
            tri_vtx[itri1] = tri_vtx0[itri0].clone();
            vtx_flag[itri1] = vtx_flag0[itri0];
            assert!(vtx_flag[itri1] != flag);
        }
    }
    for itri1 in 0..ntri1 {
        for ifatri in 0..3 {
            if tri_vtx[itri1].s[ifatri] == std::usize::MAX {
                continue;
            }
            let itri_s0 = tri_vtx[itri1].s[ifatri];
            assert!(itri_s0 < tri_vtx0.len());
            let jtri0 = map01[itri_s0];
            assert!(jtri0 < tri_vtx.len());
            tri_vtx[itri1].s[ifatri] = jtri0;
        }
    }
}

